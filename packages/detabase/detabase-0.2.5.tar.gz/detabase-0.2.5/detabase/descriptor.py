from __future__ import annotations

__all__ = ['Descriptor', 'HiddenField', 'DetaModelField', 'DateField', 'DateTimeField', 'TitleField', 'EnumField',
           'CheckBoxField', 'AutoField', 'StringField', 'RegexField', 'IntField', 'FloatField', 'NumberField']

import datetime
from functools import partial
from dataclasses import MISSING
from typing import ClassVar, Optional, Union, Any, Callable, Literal, get_type_hints
from abc import ABC

from smartjs.functions import *
from smartjs.base import *
from smartjs.elements import *

from detabase.constants import *
from detabase.protocols import *
from detabase.casting import *
from detabase.types import *
from detabase.context import *


class Descriptor(ABC):
    HTML_TAG: ClassVar[Optional[LiteralFormField]] = None
    INPUT_TYPE: ClassVar[Optional[LiteralInputType]] = None
    PARSER: ClassVar[Parser] = cast
    FINAL_TYPE: ClassVar[Optional[type]] = None
    HTMX: ClassVar[bool] = False
    DATALIST: ClassVar[bool] = False
    OPTIONS: ClassVar[bool] = False
    IS_ENUM: ClassVar[bool] = False
    
    def __init__(self, *args, **kwargs):
        self.args = [item for item in args if not item in [None, '']]
        self.default = kwargs.pop('default', MISSING if self.is_required else None)
        self.default_factory: Callable = kwargs.pop('default_factory', MISSING)
        self.label: Optional[str] = kwargs.pop('label', None)
        self.fieldset: Optional[str] = kwargs.pop('fieldset', None)
        self.group: Optional[str] = kwargs.pop('group', None)
        self.parser: Callable = kwargs.pop('parser', type(self).PARSER)
        self.min: Optional[Number] = kwargs.pop('min', None)
        self.max: Optional[Number] = kwargs.pop('max', None)
        self.step: Optional[Number] = kwargs.pop('step', None)
        self.max_length: Optional[int] = kwargs.pop('max_length', None)
        self.min_length: Optional[int] = kwargs.pop('min_length', None)

        if self.default_factory is not MISSING:
            self.default = None
        self.kwargs = kwargs
    
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f'_{name}'
        self.owner = owner
    
    def __set__(self, instance, value):
        if value is None:
            if self.default_factory is not MISSING:
                value = self.default_factory()
        setattr(instance, self.private_name, self.validate(value))
        
    class ValidationError(BaseException):
        pass
    
    def __get__(self, instance, owner=None):
        if instance is None:
            return self.default
        return getattr(instance, self.private_name)
    
    @property
    def type_hint(self):
        return TypeHint(get_type_hints(self.owner)[self.public_name])
    
    @property
    def model_type(self):
        return self.type_hint.expected_type
        
    def validate(self, value):
        value = self.parser(value, self.FINAL_TYPE or self.type_hint.expected_type)
        if self.type_hint.check_type(value):
            return value
        else:
            raise self.ValidationError(f'{type(self.owner).__name__}.{self.public_name} exige um tipo '
                                       f'{self.type_hint.expected_type}, que não coresponde ao encontrado para {value} '
                                       f'({type(value)}).')
    
    @property
    def is_required(self):
        return 'required' in self.args
    
    @property
    def html_tag(self):
        return None if not self.HTML_TAG else Tag(self.HTML_TAG)
    
    @property
    def input_type(self):
        return None if not self.INPUT_TYPE else InputType(self.INPUT_TYPE)
    
    @property
    def required(self):
        return 'required' if 'required' in self.args else None
    
    @property
    def multiple(self):
        return 'multiple' if 'multiple' in self.args else None
    
    @property
    def label_text(self):
        return self.label or self.public_name
    
    def htmx_config(self, instance=None):
        return ''
    
    def datalist(self):
        if self.DATALIST:
            return f'{self.model_type.item_name()}-list"'
        return ''
    
    def form_field_args(self, instance=None):
        return Arg(self.required), Arg(self.multiple), Kwarg('type', self.input_type), Kwarg('name', self.public_name), \
            Kwarg('id', self.public_name), Kwarg('list', self.datalist()) if self.datalist() else '', \
            Arg(self.htmx_config(instance)) if self.HTMX else '', \
            Klass(self.html_tag.bootstrap if not self.input_type else self.input_type.bootstrap), \
            Kwarg('placeholder', self.public_name)
    
    def form_field_element(self, instance=None):
        if self.HTMX:
            return BaseElement(*self.form_field_args(instance), Arg(self.htmx_config(instance)),
                               Tag(self.html_tag), self.form_field_value(instance))
        return BaseElement(*self.form_field_args(instance), Tag(self.html_tag), self.form_field_value(instance))
    
    def form_field_value(self, instance=None):
        value = self.__get__(instance)
        if self.INPUT_TYPE:
            if value not in [None, '', MISSING]:
                if self.INPUT_TYPE == 'checkbox':
                    return Arg('checked') if value == True or value == 'on' else ''
                return Kwarg('value', str(value))
            return ''
        elif self.IS_ENUM:
            return Text(self.model_type.options(value))

    @property
    def label_class(self):
        if self.INPUT_TYPE:
            return self.input_type.label_bootstrap
        return self.html_tag.label_bootstrap

    def label_element(self):
        id = Kwarg('id', f'{self.public_name}__label')
        if self.INPUT_TYPE == 'hidden':
                return ''
        return BaseElement(id, Tag('label'), Klass(self.label_class),
                                   Kwarg('for', self.public_name), Text(self.label_text))
  
    @property
    def form_field_container_class(self):
        if self.INPUT_TYPE == 'checkbox':
            return Klass('form-check mb-2 me-3')
        elif self.INPUT_TYPE == 'range':
            return Klass('form-control mb-2')
        else:
            return Klass('form-floating mb-2')
        
        
    def form_field(self, instance=None):
        if self.HTML_TAG:
            id = Kwarg('id', f'{self.public_name}__container')
            if self.INPUT_TYPE in ['checkbox', 'range']:
                return BaseElement(id, Tag('div'), self.form_field_container_class,
                                   elements=[self.label_element(), self.form_field_element(instance)])
            return BaseElement(id, Tag('div'), self.form_field_container_class,
                               elements=[self.form_field_element(instance), self.label_element()])
        return ''


    
class AutoField(Descriptor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        setattr(instance, self.private_name, getattr(instance, f'{self.public_name}_getter'))
    
    
class StringField(Descriptor):
    HTML_TAG = 'input'
    INPUT_TYPE = 'text'
    

class RegexField(Descriptor):
    HTML_TAG = 'input'
    INPUT_TYPE = 'text'
    
    
class TitleField(Descriptor):
    HTML_TAG = 'input'
    INPUT_TYPE = 'text'
    PARSER = lambda x, y: remove_extra_whitespaces(str(str(cast(x, y)))).title()


class HiddenField(Descriptor):
    HTML_TAG = 'input'
    INPUT_TYPE = 'hidden'
    
    
class NumberField(Descriptor):
    HTML_TAG = 'input'
    INPUT_TYPE = 'number'
    PARSER = lambda x, v: parse_to_number(x)
    
    
    @property
    def form_field_number_args(self):
        args = list()
        if self.min:
            args.append(Kwarg('min', self.min))
        if self.max:
            args.append(Kwarg('max', self.max))
        if self.step:
            args.append(Kwarg('step', self.step))
        return args
    
    def form_field_args(self, instance=None):
        return *super().form_field_args(instance=instance), *self.form_field_number_args

    
class IntField(NumberField):
    FINAL_TYPE = int
    PARSER = cast

    
class FloatField(NumberField):
    FINAL_TYPE = float
    PARSER = cast

    
class CheckBoxField(Descriptor):
    HTML_TAG = 'input'
    INPUT_TYPE = 'checkbox'
    
    
class EnumField(Descriptor):
    HTML_TAG = 'select'
    IS_ENUM = True
    
    
class DateField(Descriptor):
    HTML_TAG = 'input'
    INPUT_TYPE = 'date'
    FINAL_TYPE = datetime.date
    
    
class DateTimeField(Descriptor):
    HTML_TAG = 'input'
    INPUT_TYPE = 'datetime-local'
    FINAL_TYPE = datetime.datetime
    
    
class DetaModelField(Descriptor):
    HTML_TAG = 'input'
    INPUT_TYPE = 'text'
    FINAL_TYPE = str
    # HTMX = True
    DATALIST = True
    
    def __set__(self, instance, value):
        super().__set__(instance, value)
        if value:
            setattr(instance, self.model_type.item_name(), self.model_type.create(**get_from_context(self.model_type.table(), value)))
        else:
            setattr(instance, self.model_type.item_name(), None)

    def htmx_config(self, instance=None):
        def data_value():
            value = self.__get__(instance)
            if value not in [None, '']:
                return f'data-value="{value}"'
            return ''
        return data_value()
        # return f'hx-get="/options/{self.model_type.item_name()}" hx-trigger="load" hx-target="#{self.model_type.item_name()}-list" {data_value()}"'

