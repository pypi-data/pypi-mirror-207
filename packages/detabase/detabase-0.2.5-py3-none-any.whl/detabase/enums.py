__all__ = ['BaseEnum', 'PaymentMethod', 'Gender']


from enum import Enum
from smartjs.elements import Option
from smartjs.functions import *
from detabase.constants import *
class BaseEnum(Enum):
    
    @classmethod
    def table(cls):
        return cls.__name__
    
    def json(self):
        return self.name
    
    @property
    def key(self):
        return self.name
    
    def __str__(self):
        return self.value
    
    @classmethod
    def members(cls):
        return cls.__members__.values()
    
    @classmethod
    def options(cls, default: Option[str] = None):
        return join(
                [Option(),
                *[Option(member.key, f'{cls.__name__}.{member.key}', member.value, default == member.key) for member in cls.members()]]
        )
    
    
class Gender(BaseEnum):
    F = 'Feminino'
    M = 'Masculino'


class PaymentMethod(BaseEnum):
    CA = 'Dinheiro'
    CR = 'Crédito'
    DE = 'Débito'
    TR = 'Transferência bancária'
    CH = 'Cheque'
    PI = 'PIX'

    @classmethod
    def label(cls):
        return 'Método de Pagamento'
    
    
class BrazilState(BaseEnum):
    _ignore_ = 'BrazilState i'
    BrazilState = vars()
    for i in sorted([*BRAZIL_STATES]):
        BrazilState[i] = i
        
        
        
if __name__ == '__main__':
    print(BrazilState.options('GO'))