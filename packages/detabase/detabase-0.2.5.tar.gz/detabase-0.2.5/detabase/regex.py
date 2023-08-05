__all__ = ['Regex', 'Phone', 'CPF', 'CapitalName']

import re
from typing import Union, Iterable, Any
from collections import UserString
from smartjs.functions import *

class Regex(UserString):
    def __init__(self, value: str = ""):
        self.string = value
        super().__init__(self.render())

    def __repr__(self):
        return f'{type(self).__name__}({self.data})'
    
    @classmethod
    def normalize_whitespaces(cls, value: str):
        return ' '.join([i for i in re.split(r'\s+', value) if i]).strip()
    
    @classmethod
    def normalize_final_point(cls, value: str):
        return re.sub(r'\s+\.|\s\.', '.', value)
    
    @classmethod
    def special_join(cls, seq: Iterable[Any], sep: str = " ") -> str:
        return sep.join([str(item) for item in seq if item])
        
    
    @classmethod
    def split_lines(cls, value: str):
        return [i for i in [cls.normalize_whitespaces(i) for i in re.split(r'\n\r|\n', value)] if i]
    
    @property
    def digits(self):
        return ''.join(re.findall(r'\d', self.string))
    
    @property
    def words(self):
        return re.split(r'\s+|\s', self.string)
    
    def render(self):
        return self.string
    
    def export(self):
        return self.data
    
    
class Phone(Regex):

    @property
    def pattern(self):
        return re.compile(r'[\d|(|)|+]')
    
    def findall(self):
        return self.pattern.findall(self.string)
    
    def clean(self):
        return ''.join(self.findall())
    
    def phone_format(self):
        result = self.clean()
        if re.match(r'^([1-8][1-8])', result):
            result = f'+55({result[:2]}){result[2:]}'
        elif re.match(r'^(\(\d{2}\))', result):
            result = f'+55{result[:4]}{result[4:]}'
        if len(result) >= 8:
            result = f'{result[:-4]}-{result[-4:]}'
        return re.sub(r'[(]', ' (', re.sub(r'[)]', ') ', result)).strip()
    
    def render(self):
        return self.phone_format()

   
class CPF(Regex):
    
    def render(self):
        if len(self.digits) == 11:
            digits = self.digits
            return f'{digits[:3]}.{digits[3:6]}.{digits[6:9]}-{digits[9:]}'
        return ''


class CapitalName(Regex):
    def render(self):
        return self.normalize_final_point(self.normalize_whitespaces(self.string)).title()


class StringLines(Regex):
    def __init__(self, value: Union[str, list[str]]):
        if isinstance(value, (list, tuple, set)):
            self.string = self.special_join(value, sep='\n')
        else:
            self.string = value
        super().__init__(self.render())
    
    def render(self):
        return '\n'.join(self.split_lines(self.string))
    
    def export(self):
        return self.split_lines(self.data)



if __name__ == '__main__':
    data = """
    Meu nome é Daniel.
    Sou de Anápolis, GO.
    """
    x = StringLines(['Meu nome é Daniel.', 'Sou de Anápolis, GO.'])
    print(x)
    print(x.export())
    
    print()




