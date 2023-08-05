__all__ = [ 'DictModel', 'BaseDetaModel', 'StringListModel']

from abc import ABC
from typing import Iterable
from dataclasses import dataclass
from collections import UserDict, UserString, UserList

class StringListModel(UserList):
    def __init__(self, *args):
        self.args = [*args] if len(args) > 1 else args if isinstance(args, list) else list()
        super().__init__([str(item) for item in self.args])
        
    def append(self, item: str) -> None:
        self.data.append(item)
        
    def extend(self, other: Iterable[str]) -> None:
        self.data.extend(other)

@dataclass
class BaseDetaModel(ABC):
    pass

class DictModel(UserDict):
    def __init__(self, kwargs):
        self.data = kwargs
        super().__init__(self.data)
        
        
        
if __name__ == '__main__':
    x = DictModel(dict(name='daniel'))
    print(x)
    x['age'] = 34
    print(x)
    
    d = StringList()
    print(d)
    print(isinstance(d, list))
    