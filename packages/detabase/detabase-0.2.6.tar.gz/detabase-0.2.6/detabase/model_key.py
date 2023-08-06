__all__ = ['ModelKey', 'ProfileModelKey', 'ProviderModelKey']

from typing import ClassVar
from contextvars import ContextVar
from collections import UserString
from detabase.constants import *
from detabase.deta_model import *
from detabase.context import *
from smartjs.base import SmartList


class ModelKey(UserString):
    TABLES: ClassVar[list[str]] = None
    
    def __init__(self, value: str):
        self.value = value
        if self.value:
            self.table, self.key = self.value.split('.')
        else:
            self.table, self.key = None, None
        super().__init__(self.value)
    
    @classmethod
    def models(cls):
        return [ModelMap[item] for item in cls.TABLES]
        
    @property
    def model(self) -> DetaModel:
        return ModelMap[self.table]
    
    @property
    def contextvar(self) -> ContextVar:
        return ContextVarMap[self.table]
    
    @classmethod
    def dependants(cls) -> set[DetaModel]:
        return set(SmartList(*[model.dependants() for model in cls.models()], *cls.models()))
    
    
    def instance(self):
        return self.model.create(**get_from_context(self.table, self.key))
    
    
class ProfileModelKey(ModelKey):
    TABLES = ['Patient', 'Doctor', 'Therapist', 'Employee']
    
    
class ProviderModelKey(ModelKey):
    TABLES = ['Doctor', 'Therapist']
    

class StaffModelKey(ModelKey):
    TABLES = ['Doctor', 'Therapist', 'Employee']