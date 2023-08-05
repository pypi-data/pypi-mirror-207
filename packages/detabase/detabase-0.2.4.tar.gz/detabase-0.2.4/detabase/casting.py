__all__ = [
		'cast',
		'parse_to_int',
		'parse_to_float',
		'parse_to_bytes',
		'parse_to_date',
		'parse_to_enum',
		'parse_to_datetime',
		'parse_to_str',
        'no_value',
        'is_none',
        'is_undefined',
        'is_empty_string',
        'is_missing',
        'parse_to_number'
]

import datetime
from enum import EnumMeta, Enum
from typing import Any, Union, TypeVar
from decimal import Decimal
from dataclasses import MISSING
from detabase.constants import *
from detabase.types import *
from detabase.enums import BaseEnum
from detabase.regex import *
from smartjs.functions import *


def is_undefined(value: Any) -> bool:
    return value is Undefined

def is_none(value: Any) -> bool:
    return value is None

def is_missing(value: Any) -> bool:
    return value is MISSING

def is_empty_string(value: Any) -> bool:
    return value == ''

def no_value(value: Any) -> bool:
    return is_none(value) or is_undefined(value) or is_empty_string(value) or is_missing(value)


def cast(value: Any, cast_type: type[GenericType]) -> GenericType:
    if isinstance_of_type(cast_type):
        if cast_type is float:
            return parse_to_float(value)
        elif cast_type is int:
            return parse_to_int(value)
        elif cast_type is bytes:
            return parse_to_bytes(value)
        elif issubclass(cast_type, Regex):
            return parse_to_regex_type(value, cast_type)
        elif cast_type is str:
            return parse_to_str(value)
        elif cast_type is bool:
            return parse_to_bool(value)
        elif cast_type is datetime.date:
            return parse_to_date(value)
        elif cast_type is datetime.datetime:
            return parse_to_datetime(value)
        elif issubclass(cast_type, BaseEnum):
            return parse_to_enum(value, cast_type)
        elif is_dataclass_type(cast_type):
            return value
        else:
            try:
                return cast_type(value)
            except:
                raise TypeError(f'{cast_type} is not supported in cast function')
    else:
        if str in cast_type:
            if isinstance(value, str):
                return split_lines_parse(value)
    return value


def parse_to_bool(obj: Any) -> bool:
    if isinstance(obj, str):
        return True if obj == 'on' else False
    return bool(obj)

def parse_to_float(obj: Union[str, int, Decimal]) -> float:
    if isinstance(obj, str):
        return float(obj.replace(",", '.'))
    return float(obj)


def split_lines_parse(obj: Any) -> list[str]:
    if isinstance(obj, str):
        return split_lines(obj)
    elif not obj:
        return []


def parse_to_int(obj: Union[str, float, Decimal, datetime.datetime, datetime.date]) -> int:
    if isinstance(obj, str):
        return int(parse_to_float(obj))
    elif isinstance(obj, Decimal):
        return int(obj)
    elif isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.toordinal()


def parse_to_date(obj: Union[str, datetime.date, datetime.datetime, int]) -> datetime.date:
    if type(obj) is datetime.date:
        return obj
    if isinstance(obj, str):
        return datetime.date.fromisoformat(obj)
    elif isinstance(obj, int):
        return datetime.date.fromordinal(obj)
    elif isinstance(obj, datetime.datetime):
        return datetime.date(obj.year, obj.month, obj.day)


def parse_to_datetime(obj: Union[str, datetime.date, datetime.datetime, int]) -> datetime.datetime:
    if type(obj) == datetime.datetime:
        return obj
    elif isinstance(obj, str):
        return datetime.datetime.fromisoformat(obj)
    elif isinstance(obj, int):
        return datetime.datetime.fromordinal(obj)
    elif isinstance(obj, datetime.date):
        return datetime.datetime(obj.year, obj.month, obj.day)


def parse_to_enum(obj: Any, enum_type: EnumMeta) -> Enum:
    try:
        return enum_type[obj]
    except KeyError:
        return enum_type(obj)
    


def parse_to_regex_type(obj: Any, regex_type: type[RegexType]) -> RegexType:
    if obj is None:
        obj = ''
    return regex_type(obj)
    # try:
    #     return regex_type(obj)
    # except BaseException as e:
    #     return obj


def parse_to_bytes(obj: Union[str, bytes]) -> bytes:
    if type(obj) is bytes:
        return obj
    if isinstance(obj, str):
        return obj.encode('utf-8')


def parse_to_str(obj: Any) -> str:
    if obj is None:
        return ''
    elif type(obj) is str:
        return obj
    elif isinstance(obj, bytes):
        return obj.decode('utf-8')
    return str(obj)
    


def parse_to_number(obj: Any) -> Union[int, float]:
    if isinstance(obj, str):
        obj = obj.replace(',', '.')
        if '.' in obj:
            return parse_to_float(obj)
        else:
            return parse_to_int(obj)
    elif isinstance(obj, (float, int)):
        return obj
    elif isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.toordinal()
    return obj