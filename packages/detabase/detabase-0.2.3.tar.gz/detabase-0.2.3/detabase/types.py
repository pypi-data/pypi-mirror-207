__all__ = [
        'JsonPrimitive',
        'DetaData',
        'DetaKey',
        'ExpireAt',
        'ExpireIn',
        'Jsonable',
        'JsonSequence',
        'DetaQuery',
        'isinstance_of_type',
        'is_dataclass_instance',
        'is_dataclass_type',
		'TypeHint',
        'ExistParams',
        'SearchParam',
        'DictModelType'
]
import datetime
from dataclasses import is_dataclass
from collections import ChainMap
from typing import Union, Any, get_args, get_origin, TypeVar
from smartjs.functions import *
from detabase.regex import *
from detabase.base_models import *


JsonPrimitive = Union[str, float, int, bool, None]
DetaData = Union[dict, list, str, float, int, bool]
DetaKey = Union[str, None]
ExpireIn = Union[str, None]
ExpireAt = Union[datetime.datetime, int, float, None]
JsonSequence = list[JsonPrimitive]
JsonDict = dict[str, Union[JsonSequence, JsonPrimitive]]
Jsonable = Union[JsonDict, JsonSequence, JsonPrimitive]
DetaQuery = Union[dict[str, JsonPrimitive], list[dict[str, JsonPrimitive]]]
ExistParams = Union[list[str], str]
SearchParam = str
RegexType = TypeVar('RegexType', bound=Regex)
DictModelType = TypeVar('DictModelType', bound=DictModel)


def isinstance_of_type(obj: Any) -> bool:
    return isinstance(obj, type)


def is_dataclass_type(obj: Any) -> bool:
    return not is_dataclass_instance(obj) and is_dataclass(obj)


def is_dataclass_instance(obj: Any) -> bool:
    return is_dataclass(obj) and not isinstance_of_type(obj)


class TypeHint:
    def __init__(self, type_hint):
        self.type_hint = type_hint
    
    @property
    def args(self):
        return tuple(list_filtered(get_args(self.type_hint)))
    
    @property
    def is_args_generic(self):
        return all([not isinstance_of_type(item) for item in self.args])

    @property
    def origin(self):
        return get_origin(self.type_hint)
    
    @property
    def is_sequence(self):
        return self.origin in (list, tuple)
    
    @property
    def is_mapping(self):
        return self.origin in (dict, ChainMap)
    
    @property
    def is_generic(self):
        return not isinstance_of_type(self.origin)
    
    @property
    def is_simple_type(self) -> bool:
        return not self.args and isinstance_of_type(self.type_hint)
    
    @property
    def is_optional(self):
        return type(None) in self.args
    
    @property
    def expected_type(self):
        if self.is_simple_type:
            return self.type_hint
        return self.args
    
    @property
    def is_dict_model(self):
        return issubclass(self.type_hint, DictModel)
    
    @property
    def is_deta_model(self):
        return issubclass(self.type_hint, BaseDetaModel)
    
    @property
    def is_string_list_model(self):
        return issubclass(self.type_hint, StringListModel)
    
    def check_type(self, value: Any) -> bool:
        if self.is_simple_type:
            if self.is_deta_model:
                return isinstance(value, str)
            elif self.is_dict_model:
                return isinstance(value, dict)
            elif self.is_string_list_model:
                return isinstance(value, list) and all([isinstance(item, str) for item in value])
            return isinstance(value, self.type_hint)
        elif self.is_generic:
            return isinstance(value, self.args)
        elif self.is_sequence:
            return isinstance(value, self.origin) and all([isinstance(item, self.args) for item in value])
        elif self.is_mapping:
            return isinstance(value, self.origin) and all(
                    [isinstance(item, tuple(self.args[1:])) for item in value.values()]) and all(
                    [isinstance(item, self.args[0]) for item in value.keys()])
        else:
            return False

