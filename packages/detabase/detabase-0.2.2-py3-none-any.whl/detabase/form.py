from __future__ import annotations

__all__ = ['Form']

from smartjs.base import *
from smartjs.functions import *
from detabase.types import *

class Form(BaseElement):
    def __init__(self, instance: 'DetaModel', *args, **kwargs):
        if is_dataclass_instance(instance):
            self.instance = instance
            self.model = type(instance)
            self.action = Kwarg('action', f'/form/update/{self.model.item_name()}/{getattr(self.instance, "key")}')
            self.id = Kwarg('id', f'{self.model.table()}Update')
        else:
            self.model = instance
            self.instance = None
            self.action = Kwarg('action', f'/form/new/{self.model.item_name()}')
            self.id = Kwarg('id', f'{self.model.table()}New')

        self.form_fields = list_filtered([item.form_field(self.instance) for item in self.model.form_field_descriptors().values()])
        super().__init__(*args, Klass('form-control'), **kwargs)
        self.elements.extend(self.form_fields)
        self.args.extend([self.action, self.id, Kwarg('method', 'post')])