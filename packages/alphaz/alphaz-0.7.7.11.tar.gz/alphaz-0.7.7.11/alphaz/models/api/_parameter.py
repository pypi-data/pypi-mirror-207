import json, datetime, dataclasses, re, sqlalchemy, xmltodict

from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy import inspect as inspect_sqlalchemy

from flask import request
from collections.abc import Callable

from ..main import AlphaException
from ..main._base import is_dataclass
from ..main._enum import MappingMode

from ...libs import date_lib, json_lib, py_lib

from enum import Enum


def dict_to_model(model, parameters):
    from core import core

    inspected = inspect_sqlalchemy(model)

    """for key, col in dict(model.__dict__).items():
    if not hasattr(col, "prop"):
        continue

    binary_expression = type(col.expression) is BinaryExpression
    column_property = isinstance(col.prop, ColumnProperty)-

    if not relationship and (column_property and not binary_expression):
        attributes[key] = col"""

    #! TOTO: modify
    """if disabled_relationships:
        if (column_property or isinstance(col.prop, RelationshipProperty)) and not binary_expression and key not in disabled_relationships:
            attributes[key] = col"""
    for relationship, relationship_property in inspected.relationships.items():
        if relationship in parameters:
            relationship_table_name = relationship_property.target.key
            relationship_model = core.db.get_table_model(relationship_table_name)
            parameters[relationship] = dict_to_model(
                relationship_model, parameters[relationship]
            )
    M = (
        model(**{x: y for x, y in parameters.items() if x in model.__dict__})
        if type(parameters) != list
        else [
            model(**{x: y for x, y in p.items() if x in model.__dict__})
            for p in parameters
        ]
    )
    return M  # TODO: enhanced multi rel


def set_value_like_mode(value, mode):
    if value is None:
        return None
    value = str(value).replace("*", "%")

    if not value.startswith("%") and mode in [
        ParameterMode.IN_LIKE,
        ParameterMode.START_LIKE,
    ]:
        value = f"%{value}"

    if not value.endswith("%") and mode in [
        ParameterMode.IN_LIKE,
        ParameterMode.END_LIKE,
    ]:
        value = f"{value}%"
    return value


class ParameterMode(Enum):
    NONE = 0
    LIKE = 1
    IN_LIKE = 2
    START_LIKE = 3
    END_LIKE = 4

    def __str__(self):
        return str(self.value)

    def to_json(self):
        return str(self.value)


class Parameter:
    _value = None
    no_log: bool = False

    def __init__(
        self,
        name: str,
        default=None,
        empty_value=None,
        none_value=None,
        options=None,
        cacheable: bool = True,
        required: bool = False,
        ptype: type = str,
        private: bool = False,
        mode: ParameterMode = ParameterMode.NONE,
        override: bool = False,
        function: Callable = None,
        mapping_mode: MappingMode | str | None = None,
        map_none: bool = False,
        max_size: int | None = None,
        min_size: int | None = None,
        separators: list = [",", ";"],
    ):
        """[summary]

        Args:
            name (str): [description]
            default ([type], optional): [description]. Defaults to None.
            options ([type], optional): [description]. Defaults to None.
            cacheable (bool, optional): [description]. Defaults to True.
            required (bool, optional): [description]. Defaults to False.
            ptype (type, optional): [description]. Defaults to str.
            private (bool, optional): [description]. Defaults to False.
            mode (str, optional): [description]. Defaults to "none".
        """
        self.name = name
        self.default = default
        self.cacheable = cacheable
        self.empty_value = empty_value
        self.none_value = none_value
        self.options = options
        self.required = required
        self.ptype: type = ptype
        self.function: Callable = function
        self.type = str(ptype).replace("<class '", "").replace("'>", "")
        self.private = private
        self.mode = mode
        self.override = override
        self.is_value = False
        self.mapping_mode = mapping_mode
        self.max_size = max_size
        self.min_size = min_size
        self.map_none = map_none

    @property
    def value(self):
        return self._value if self._value is not None else self.default

    def __check_options(self, value):
        if (
            self.options is not None
            and value not in self.options
            and not (not self.required and value is None)
        ):
            raise AlphaException(
                "api_wrong_parameter_option",
                parameters={
                    "value": value,
                    "parameter": self.name,
                    "options": str(self.options),
                },
            )

    def set_value(self, method: str, dataDict, api_json, form, args):
        """Set parameter value

        Raises:
            AlphaException: [description]
        """
        # dataDict: for list GET
        self._value = self.default
        self.name = self.name.strip()
        dataDict = {x.strip(): y for x, y in dataDict.items()}

        if "<xml>" in str(request.data):
            try:
                data = xmltodict.parse(request.data)
                if self.name in data["xml"]:
                    self._value = data["xml"][self.name]
            except:
                pass

        if form is not None and self.name in form:
            self._value = form[self.name]
            self.is_value = True
        elif api_json is not None and self.name in api_json:
            self._value = api_json[self.name]
            self.is_value = True
        elif (
            self.name in args
            and self.name in dataDict
            and (self.ptype == list or py_lib.is_subtype(self.ptype, list))
            and (len(dataDict[self.name]) != 1)
        ):
            self._value = dataDict[self.name]
            self.is_value = True
        elif self.name in args:
            self._value = args.get(self.name)
            self.is_value = True
        elif self.name in dataDict:
            self._value = dataDict[self.name]
            self.is_value = True

        # check size
        if (
            self.max_size is not None
            and self._value is not None
            and len(self._value) > self.max_size
        ):
            raise AlphaException(
                "api_parameter_length_too_long",
                parameters={
                    "parameter": self.name,
                    "size": len(self.value),
                    "value": self._value,
                    "max": self.max_size,
                },
            )
        if (
            self.min_size is not None
            and self._value is not None
            and len(self._value) < self.min_size
        ):
            raise AlphaException(
                "api_parameter_length_too_long",
                parameters={
                    "parameter": self.name,
                    "size": len(self.value),
                    "value": self._value,
                    "min": self.min_size,
                },
            )

        # list
        if self.ptype == list or py_lib.is_subtype(self.ptype, list):
            is_empty = self._value is None or str(self._value).strip() == ""
            is_empty_value = all(not x in str(self._value) for x in [";", ",", "["])

            if is_empty:
                self._value = self.default
            elif is_empty_value:
                self._value = (
                    dataDict[self.name] if self.name in dataDict else self.default
                )

            sub_type = py_lib.get_subtype(self.ptype)
            if is_dataclass(sub_type):
                if self._value is not None:
                    values = re.findall(r"{[^{]*}", str(self._value))
                    self._value = self.default if len(values) == 0 else []
                    for val in values:
                        if hasattr(sub_type, "map_from_json"):
                            val = sub_type.map_from_json(
                                val, mapping_mode=self.mapping_mode
                            )
                        else:
                            P = json.loads(val)
                            val = sub_type(**P)
                        self._value.append(val)
                else:
                    self._value = self.default

        if self._value is None and form is not None and self.name in form:
            self._value = form[self.name]
        if self._value is None and form is not None and self.name in form:
            self._value = form[self.name]

        if isinstance(self.ptype, DeclarativeMeta):
            if self._value is None:
                parameters = {x: y for x, y in form.items() if hasattr(self.ptype, x)}
            else:
                parameters = (
                    self._value
                    if type(self._value) == dict
                    else json_lib.load_json(self._value)
                )
                parameters = {
                    x: y
                    for x, y in parameters.items()
                    if hasattr(self.ptype, x) and (self.map_none or y is not None)
                }  # TODO: enhance
            self._value = dict_to_model(self.ptype, parameters)
        elif is_dataclass(self.ptype):
            if hasattr(self.ptype, "map_from_json"):
                self._value = self.ptype.map_from_json(
                    self._value, mapping_mode=self.mapping_mode
                )
            else:
                P = json.loads(self._value)
                self._value = self.ptype(**P)

        if self.ptype == dict:
            self._value = json_lib.load_json(self._value)

        if self.required and (self._value is None or str(self._value) == "undefined"):
            raise AlphaException(f"Missing parameter {self.name}")

        if self._value is None:
            self.__check_options(self._value)
            return

        if str(self._value).lower() in ["null", "none", "undefined"]:
            self._value = self.none_value if self.is_value else None
        if str(self._value).lower() in ["null()"]:
            self._value = sqlalchemy.null()
        if self.empty_value is not None and str(self._value).lower() == "":
            self._value = self.empty_value

        if self.ptype == str and (
            self.mode
            in [
                ParameterMode.LIKE,
                ParameterMode.IN_LIKE,
                ParameterMode.START_LIKE,
                ParameterMode.END_LIKE,
            ]
        ):
            self._value = set_value_like_mode(self._value, self.mode)

        if self.ptype == bool:
            str_value = str(self._value).lower()
            self.__check_options(str(self._value))

            if str_value in ["y", "true", "t", "1"]:
                value = True
            elif str_value in ["n", "false", "f", "0"]:
                value = False
            else:
                raise AlphaException(
                    f"Wrong value <{self._value}> for parameter <{self.name}> of type <bool>",
                )
            self._value = value

        if self.ptype == list or py_lib.is_subtype(self.ptype, list):
            if type(self._value) == str and str(self._value).strip() == "":
                self._value = []
            elif type(self._value) == str:
                try:
                    if (
                        len(str(self._value)) != 0
                        and str(self._value)[0] == "["
                        and str(self._value)[-1] == "]"
                    ):
                        self._value = (
                            str(self._value)[1:-1].split(";")
                            if ";" in str(self._value)
                            else str(self._value)[1:-1].split(",")
                        )
                    elif ";" in str(self._value) or "," in str(self._value):
                        self._value = (
                            str(self._value).split(";")
                            if ";" in str(self._value)
                            else str(self._value).split(",")
                        )
                    else:
                        self._value = [self._value]
                except:
                    raise AlphaException(
                        f"Wrong value <{self._value}> for parameter <{self.name}> of type <list>"
                    )

            if py_lib.is_subtype(self.ptype, list[int]):
                self._value = [int(x) for x in self._value]
            if py_lib.is_subtype(self.ptype, list[float]):
                self._value = [float(x) for x in self._value]

            for val in self._value:
                self.__check_options(val)

            if self.mode in [
                ParameterMode.LIKE,
                ParameterMode.IN_LIKE,
                ParameterMode.START_LIKE,
                ParameterMode.END_LIKE,
            ]:
                self._value = [set_value_like_mode(x, self.mode) for x in self._value]

        if self.ptype == int:
            try:
                self._value = int(self._value) if self._value is not None else None
            except:
                raise AlphaException(
                    f"Wrong value <{self._value}> for parameter <{self.name}> of type <int>"
                )
            self.__check_options(self._value)

        if self.ptype == float:
            try:
                self._value = float(self._value)
            except:
                raise AlphaException(
                    f"Wrong value <{self._value}> for parameter <{self.name}> of type <float>"
                )
            self.__check_options(self._value)

        if self.ptype == datetime.datetime:
            self.__check_options(self._value)
            self._value = date_lib.str_to_datetime(self._value)

        if hasattr(self.ptype, "metadata") and not hasattr(self._value, "metadata"):
            r = json.loads(self._value)
            self._value = self.ptype(**r)

        if self.ptype == str:
            self.__check_options(str(self._value))

        if self.function is not None:
            self._value = self.function(self._value)
