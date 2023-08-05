from __future__ import annotations

__all__ = ['is_detamodel_type', 'is_detamodel_instance', 'is_detamodel', 'Descriptor', 'DetaModel']

import re
from dataclasses import dataclass, fields, Field, asdict
from typing import ClassVar, Optional, Union, Any, get_type_hints
from collections import ChainMap
from abc import ABC
from unidecode import unidecode
from typing_extensions import Self
from detabase.types import *
from detabase.json_encoder import *
from detabase.descriptor import *
from detabase.engine import *
from detabase.context import *
from detabase.base_models import *
from smartjs.base import SmartList
from smartjs.functions import *

def make_base_query(instance: DetaModel, params_string: str) -> DetaQuery:
    result = dict_filtered({key: getattr(instance, key, None) for key in params_string.split() if getattr(instance, key, None)})
    return result

def exist_query(instance: DetaModel, params: ExistParams) -> DetaQuery:
    assert params, f'cadastrar EXIST_PARAMS na classe {instance.class_name()}'
    if isinstance(params, list):
        deta_query = list()
        for item in params:
            deta_query.append(make_base_query(instance, item))
        cleaned = list_filtered(deta_query, func=lambda x: len(x) >= 1)
        return cleaned[0] if len(cleaned) == 1 else cleaned
    return make_base_query(instance, params)
    
def is_detamodel(obj: Any) -> bool:
    return True if is_detamodel_instance(obj) or is_detamodel_type(obj) else False
    
    
def is_detamodel_type(obj: Any) -> bool:
    return True if isinstance_of_type(obj) and issubclass(obj, DetaModel) else False


def is_detamodel_instance(obj: Any) -> bool:
    return True if not isinstance_of_type(obj) and isinstance(obj, DetaModel) else False


def has_detamodel(type_hint):
    types = TypeHint(type_hint).expected_type
    if isinstance(types, tuple):
        for item in types:
            if isinstance_of_type(item):
                if issubclass(item, DetaModel):
                    return True
    else:
        if isinstance_of_type(types):
            if issubclass(types, DetaModel):
                return True
    return False


def dependants(detamodel: type[DetaModel]):
    hints = get_type_hints(detamodel)
    for hint in hints.values():
        if has_detamodel(hint):
            yield TypeHint(hint).expected_type


def dependants_list(detamodel: type[DetaModel]):
    result = SmartList()
    for item in list(dependants(detamodel)):
        result.include(item)
    return [*set(result.data)]

    
@dataclass
class DetaModel(BaseDetaModel):
    TABLE: ClassVar[Optional[str]] = None
    DETA_QUERY: ClassVar[Optional[DetaQuery]] = None
    PLURAL: ClassVar[Optional[str]] = None
    SINGULAR: ClassVar[Optional[str]] = None
    ITEM_NAME: ClassVar[Optional[str]] = None
    EXIST_PARAMS: ClassVar[Optional[ExistParams]] = None
    SEARCH_PARAM: ClassVar[SearchParam] = 'search'
    PRIVATE_PARAMS: ClassVar[Optional[str]] = None
    HASH_PARAMS: ClassVar[Optional[str]] = None
    
    @property
    def search_getter(self):
        return normalize(str(self)).lower()
    
    def __lt__(self, other):
        return self.normalize_lower_case(str(self)) < self.normalize_lower_case(str(other))
        

    def json_parse(self) -> Jsonable:
        return json_parse(self)
    
    def json_dumps(self) -> str:
        return json_dumps(self)
    
    @staticmethod
    def json_loads(string: str) -> dict:
        return json_loads(string)
    
    @classmethod
    def bases(cls):
        return [item for item in reversed(cls.mro()) if issubclass(item, DetaModel)]
    
    @classmethod
    def class_name(cls):
        return cls.__name__
    
    @classmethod
    def fields(cls: Union[type[DetaModel], DetaModel]) -> dict[str, Field]:
        return {item.name: item for item in fields(cls)}
    
    @classmethod
    def all_fields(cls) -> dict[str, Field]:
        return vars(cls)['__dataclass_fields__']
    
    @classmethod
    def descriptors(cls):
        mapping = ChainMap(*[vars(item) for item in [m for m in cls.bases() if issubclass(m, DetaModel)]])
        return {key: value for key, value in mapping.items() if isinstance(value, Descriptor)}
    
    @classmethod
    def init_fields(cls):
        return {key: value for key, value in cls.all_fields().items() if not str(value.type).__contains__('ClassVar')}

    @classmethod
    def init_var_fields(cls):
        return {key: value for key, value in cls.all_fields().items() if str(value.type).__contains__('InitVar')}

    @classmethod
    def class_var_fields(cls):
        return {key: value for key, value in cls.all_fields().items() if str(value.type).__contains__('ClassVar')}
    
    @classmethod
    def form_field_descriptors(cls):
        return {key: value for key, value in cls.descriptors().items() if value.html_tag}
    
    @classmethod
    def table(cls):
        return cls.TABLE or cls.class_name()
    
    @classmethod
    def item_name(cls) -> str:
        return cls.ITEM_NAME or cls.slug(cls.table())
    
    @classmethod
    def key_name(cls) -> str:
        return f'{cls.item_name()}_key'
    
    @staticmethod
    def normalize(string: str) -> str:
        return unidecode(string)
    
    @staticmethod
    def normalize_lower_case(string: str) -> str:
        return DetaModel.normalize(string).lower()
    
    @staticmethod
    def join_strings(string_list: list[Union[str, Any]], sep=" ") -> str:
        return sep.join([str(item) for item in string_list if item not in [None, '']])
    
    @staticmethod
    def slug(string: str) -> str:
        return DetaModel.normalize_lower_case(DetaModel.join_strings(re.split(r'([A-Z][a-z]+)(?=[A-Z])|\s', string), sep="_"))

    @classmethod
    def dependants(cls):
        result = dependants_list(cls)
        for item in result:
            result.extend(dependants_list(item))
        return result
    
    @classmethod
    async def fetch_all(cls, query: DetaQuery = None) -> list[Jsonable]:
        return await DetaBase(cls.table()).fetch_all(query=query or cls.DETA_QUERY)
    
    @classmethod
    async def fetch(cls, query: DetaQuery = None, last: Optional[str] = None, limit: int = 1000):
        return await DetaBase(cls.table()).fetch(query=query or cls.DETA_QUERY, last=last, limit=limit)

    @classmethod
    async def instance(cls, key: str) -> Self:
        if key is None:
            raise Exception(f'{cls.class_name()}.instance method needs a key argument.')
        else:
            await cls.update_context()
            result = await cls.get_data(key)
            if not result:
                raise Exception(f'A chave {key} não foi encontrada na tabela {cls.table()}.')
            return cls.create(**result)

    @classmethod
    async def update_context(cls):
        await update_context([item.class_name() for item in [cls, *cls.dependants()]])

    @classmethod
    def create(cls, *args, **kwargs) -> Self:
        try:
            return cls(*args, **kwargs)
        except BaseException as e:
            print(e)
            return cls(*args, **cls._filter_initfields(kwargs))
        
    @classmethod
    def _filter_initfields(cls, data: dict):
        return {key: value for key, value in data.items() if key in cls._initfields_names()}

    @classmethod
    def _initfields_names(cls) -> list[str]:
        return [*cls._initvars_names(), *cls._fields_names()]
    
    @classmethod
    def _fields_names(cls) -> Optional[list[str]]:
        return list(cls.fields().keys())

    @classmethod
    def _initvars_names(cls) -> list[str]:
        return list(cls.init_var_fields().keys())

    @classmethod
    async def get_data(cls, key: str) -> Optional[dict[str, Jsonable]]:
        if not key:
            raise ValueError(f'{cls.class_name()}.get_data method need a key argument')
        return await DetaBase(cls.table()).get(key)

    @classmethod
    async def instances_list(cls, query: DetaQuery = None) -> list[Optional[Self]]:
        await cls.update_context()
        result = await cls.fetch_all(query)
        try:
            return sorted([cls.create(**item) for item in result])
        except BaseException as e:
            print(e)
            return [cls.create(**item) for item in result]
        
    def exist_query(self):
        return exist_query(self, self.EXIST_PARAMS)
        
    async def exist_search(self):
        return await self.instances_list(exist_query(self, self.EXIST_PARAMS))
    
    def asdict_non_private(self):
        if self.PRIVATE_PARAMS:
            return {k: v for k, v in asdict(self).items() if k not in self.PRIVATE_PARAMS.split()}
        return asdict(self)
    
    async def exist(self):
        exist = await self.exist_search()
        if len(exist) == 1:
            return exist[0]
        elif len(exist) > 1:
            raise ValueError(f'{self.table()} trouxe mais que um item ({exist}). O permitido é um ou nenhum')
        else:
            return None
        
    async def save_new(self):
        exist = await self.exist()
        if exist:
            raise ValueError(f'{exist} já existe no banco de dados com a chave {getattr(exist, "key")} com os dados {exist.asdict_non_private()}')
        data = await DetaBase(self.table()).insert(data=self.json_parse())
        if data:
            return self.create(**data)
        return None
    
    async def update(self, data: dict):
        assert getattr(self, 'key'), 'é necessário uma chave salva para atualizar a instância no banco de dados'
        locked = ' '.join(list_filtered(['key', self.HASH_PARAMS])).split()
        for item in data:
            if not item in locked:
                setattr(self, item, data[item])
        updated = await DetaBase(self.table()).put(data=self.json_parse())
        if updated:
            return self.create(**updated)
        raise ValueError(f'Os dados de {self} não foram atualizados por algum erro.')
        
    @classmethod
    async def delete_key(cls, key: str):
        return await DetaBase(cls.table()).delete(key)
    
    async def delete_self(self):
        return await self.delete_key(getattr(self, "key"))
    
    @classmethod
    def singular(cls):
        return cls.SINGULAR or cls.class_name()
    
    @classmethod
    def plural(cls):
        return cls.PLURAL or f'{cls.singular()}s'

