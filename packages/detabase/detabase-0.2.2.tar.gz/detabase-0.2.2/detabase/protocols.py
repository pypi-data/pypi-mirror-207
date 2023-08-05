__all__ = ['Parser', 'Validator']


from typing import Protocol, Any, Union
from starlette.requests import Request
from starlette.responses import Response
from detabase.constants import GenericType


class Parser(Protocol):
	def __call__(self, value: Any, final_type: type[GenericType]) -> GenericType:
		...

class Validator(Protocol):
	def __call__(self, value: GenericType, types: Union[type, tuple[type]]) -> GenericType:
		...
	
	
class Endpoint(Protocol):
	def __await__(self, request: Request) -> Response:
		...