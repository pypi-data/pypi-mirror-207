from __future__ import annotations

__all__ = ['Form']

from smartjs.base import *
from smartjs.functions import *
from detabase.types import *
from smartjs.elements import Heading

class Form(BaseElement):
    def __init__(self, instance: 'DetaModel', *args, **kwargs):
        elements = kwargs.pop('elements', list())
        args = [*args]
        if is_dataclass_instance(instance):
            self.instance = instance
            self.model = type(instance)
            self.form_title = Heading(3, Text(f'Atualizar {self.model.singular()}'))
            self.action = Kwarg('action', f'/form/update/{self.model.item_name()}/{getattr(self.instance, "key")}')
            self.id = Kwarg('id', f'{self.model.table()}Update')
            self.button = BaseElement(Tag('button'), Klass('btn btn-warning form-control update'), Text('atualizar'))
        else:
            self.model = instance
            self.instance = None
            self.form_title = Heading(3, Text(f'Adicionar {self.model.singular()}'))
            self.action = Kwarg('action', f'/form/new/{self.model.item_name()}')
            self.id = Kwarg('id', f'{self.model.table()}New')
            self.button = BaseElement(Tag('button'), Klass('btn btn-warning form-control new'), Text('salvar'))

        self.form_fields = list_filtered([item.form_field(self.instance) for item in self.form_field_descriptors().values()])
        elements.append(self.form_title)
        elements.extend(self.form_fields)
        elements.extend(self.datalists)
        elements.append(self.button)
        args.extend([self.action, self.id, Kwarg('method', 'post'), Klass('form-control')])
        super().__init__(*args, elements=elements, **kwargs)

    @property
    def form_field_descriptors(self):
        return self.model.form_field_descriptors()
    @property
    def datalists(self):
        models = {item.model_type for item in self.form_field_descriptors.values() if item.DATALIST}
        return [BaseElement(Tag('datalist'), Kwarg('id', f'{model.item_name()}-list'), Kwarg('hx-get', f'/options/{model.item_name()}'), Kwarg('hx-trigger', 'load')) for model in models]
        