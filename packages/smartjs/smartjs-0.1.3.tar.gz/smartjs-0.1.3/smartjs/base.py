from __future__ import annotations

__all__ = [
        'Tag',
        'InputType',
        'SmartList',
        'BaseScript',
        'BaseElement',
        'BaseArg',
        'Arg',
        'Kwarg',
        'Klass',
        'Text',
        'StyleItem',
        'BaseStyle',
        'SmartSet',
        'Id',
        'Name',
        'HxConfig'
]

from enum import Enum
from typing import Union, Optional
from collections import UserString
from smartjs.constants import *
from smartjs.functions import *
from smartjs.collection import *


class Tag(Enum):
    """
    Tag(Enum):
    property: is_empty
    property: is_form_field
    property: is_input
    property: bootstrap
    property: label_bootstrap
    """
    _ignore_ = 'Tag i'
    Tag = vars()
    for i in TAGS:
        Tag[f'{i}'.upper()] = i
    
    def __str__(self):
        return self.value
    
    @property
    def is_empty(self):
        return self.value in EMPTY_TAGS
    
    @property
    def is_form_field(self):
        return self.value in FORM_FIELDS
    
    @property
    def is_input(self):
        return self.value == 'input'
    
    @property
    def bootstrap(self):
        if self.is_form_field:
            if self.value == 'select':
                return 'form-select'
            elif self.value == 'textarea':
                return 'form-control'
        return None
    
    @property
    def label_bootstrap(self):
        if self.value == 'select':
            return ''
        return 'form-label'


class InputType(Enum):
    """
    InputType(Enum):
    property: bootstrap
    property: label_bootstrap
    """
    _ignore_ = 'InputType i'
    InputType = vars()
    for i in INPUT_TYPES:
        InputType[f'{i}'.upper().replace("-", "_")] = i
    
    def __str__(self):
        return self.value
    
    @property
    def bootstrap(self):
        if self.value == 'checkbox':
            return 'form-check-input'
        elif self.value == 'color':
            return 'form-control form-control-color'
        elif self.value == 'range':
            return 'form-range'
        return 'form-control'
    
    @property
    def label_bootstrap(self):
        if self.value == 'checkbox':
            return f'form-check-label'
        return 'form-label'


class BaseArg(UserString):
    """
    BaseArg(Userstring):
    derived classes:
    - Arg(BaseArg)
    - Kwarg(BaseArg)
    - Klass(BaseArg)
    - Text(BaseArg)
    - StyleItem(BaseArg)
    """


class Arg(BaseArg):
    """
    arguments for BaseElement
    """
    
    def __init__(self, *args):
        super().__init__(join(args, sep=" "))


class Kwarg(BaseArg):
    """
    key value pairs for BaseElement tag config
    """
    
    def __init__(self, *args):
        self.args = [*args]
        super().__init__(
            self.args[0] if len(self.args) == 1 else f'{underscore_to_hyphen(self.args[0])}="{self.args[1]}"')


class Klass(BaseArg):
    """
    class attribute of BaseElement
    """
    
    def __init__(self, *args):
        super().__init__(join(args, sep=" "))


class StyleItem(BaseArg):
    """
    head style and inline style key value item
    """
    
    def __init__(self, *args):
        self.args = [*args]
        super().__init__(
            self.args[0] if len(self.args) == 1 else f'{underscore_to_hyphen(self.args[0])}: {self.args[1]}')


class Text(BaseArg):
    """
    node text for BaseElement as innerText
    """
    
    def __init__(self, *args):
        super().__init__(join(args))


class Id(BaseArg):
    def __init__(self, value: str):
        if value:
            super().__init__(f'id="{value}"')
        else:
            super().__init__('')
        
        
class Name(BaseArg):
    def __init__(self, value: str):
        if value:
            super().__init__(f'name="{value}"')
        else:
            super().__init__('')
    
    
class HxConfig(BaseArg):
    def __init__(self,
                 get: str = None,
                 post: str = None,
                 trigger: str = None,
                 target: str = None,
                 swap: str = None,
                 swap_oob: Union[True, str] = None,
                 indicator: str = None,
                 vals: str = None,
                 on: str = None,
                 select: str = None,
                 select_oob: str = None,
                 push_url: bool = None,
                 ):
        self.get = f'hx-get="{get}"' if get else None
        self.post = f'hx-post="{post}"' if post else None
        self.trigger = f'hx-trigger="{trigger}"' if trigger else None
        self.target = f'hx-target="#{target}"' if target else None
        self.swap = f'hx-swap="{swap}"' if swap else None
        self.swap_oob = f'hx-swap-oob="{swap_oob}"' if select_oob else None
        self.indicator = f'hx-indicator="#{indicator}"' if indicator else None
        self.vals = "hx-vals='{}'".format(vals) if vals else None
        self.on = 'hx-on="{}"'.format(on) if on else None
        self.select = f'hx-select="#{select}"' if select else None
        self.select_oob = f'hx-select-oob="#{select_oob}"' if select_oob else None
        self.push_url = f'hx-push-url="true"' if push_url is True else f'hx-push-url="false"' if push_url is False else None
        super().__init__(join([self.get, self.post, self.trigger, self.target, self.swap, self.indicator, self.vals,
                               self.on, self.push_url, self.select, self.select_oob, self.swap_oob
                               ]))
    

class BaseScript(UserString):
    
    @classmethod
    def slug_case(cls, name: str):
        return slug(name)
    
    @classmethod
    def cap_words_case(cls, name: str):
        return cap_words_case(name)
    
    @classmethod
    def camel_case(cls, name: str):
        return camel_case(name)
    
    @classmethod
    def get_computed_style(cls, element_name: str):
        return f'getComputedStyle({element_name})'
    
    @classmethod
    def remove(cls, element_name: str):
        return f'{element_name}.remove()'
    
    @classmethod
    def scroll(cls, element_name: str, x: int, y: int):
        return f'{element_name}.scroll({x}, {y})'
    
    @classmethod
    def set_html(cls, element_name: str, html: str):
        return f'{element_name}.setHTML({html})'
    
    @classmethod
    def scroll_to(cls, element_name: str, x: int, y: int):
        return f'{element_name}.scrollTo({x}, {y})'
    
    @classmethod
    def scroll_by(cls, element_name: str, x: int, y: int):
        return f'{element_name}.scrollBy({x}, {y})'
    
    @classmethod
    def replace_with(cls, element_out: str, element_in):
        return f'{element_out}.replaceWith({element_in})'
    
    @classmethod
    def remove_attribute(cls, element_name: str, attribute: str):
        return f'{element_name}.removeAttribute("{attribute}")'
    
    @classmethod
    def const_by_query_selector(cls, element_name: str, selector: str):
        return cls.const(element_name, f'querySelector("{selector}")')
    
    @classmethod
    def const_by_query_selector_all(cls, element_name: str, selector: str):
        return cls.const(element_name, f'querySelectorAll("{selector}")')
    
    @classmethod
    def const_by_tag_name(cls, element_name, tag_name):
        return cls.const(element_name, f'getElementsByTagName("{tag_name}")')
    
    @classmethod
    def const_by_id(cls, element_id: str):
        return f'const {cls.camel_case(element_id)} = document.getElementById("{element_id}")'
    
    @classmethod
    def const_get_attribute(cls, selection_name: str, element_name: str, attribute: str):
        return f'const {selection_name} = {element_name}.getAttribute("{attribute}")'
    
    @classmethod
    def set_interval(cls, function_name: str, interval: int = 1000):
        return f'setInterval({function_name}, {interval})'
    
    @classmethod
    def for_loop(cls, item_name: str, array_name: str, statements: list[str]):
        return f'for (const {item_name} of {array_name}) {{{join(statements, "; ")}}}'
    
    @classmethod
    def set_timeout(cls, function_name: str, timeout: int = 1000):
        return f'setTimeout({function_name}, {timeout})'
    
    @classmethod
    def function(cls, name: str, arguments: str = "", statements: list[str] = None):
        return f'function {name} ({arguments}) {{{join(statements, "; " )}}}'
    
    @classmethod
    def anonymous(cls, arguments: str = "", statements: list[str] = None):
        return f'({arguments}) => {{{join(statements, "; " )}}}'
    
    @classmethod
    def if_statement(cls, condition: str, statements: list[str]):
        return f'if({condition}){{{join(statements, "; ")}}}'
    
    @classmethod
    def else_if_statement(cls, condition: str, statements: list[str]):
        return f'else if({condition}){{{join(statements, "; ")}}}'
    
    @classmethod
    def else_statement(cls, statements: list[str]):
        return f'else {{{join(statements, "; ")}}}'
    
    @classmethod
    def const_create_element(cls, name: str, tag: str):
        return f'const {name} = document.createElement("{tag}")'
    
    @classmethod
    def let(cls, element_name: str, statement: str):
        return f'let {element_name} = {statement}'
    
    @classmethod
    def const(cls, element_name: str, statement: str):
        return f'const {element_name} = {statement}'
    
    @classmethod
    def set_class_name(cls, element_name: str, class_name: str):
        return f'{element_name}.className = "{class_name}"'
    
    @classmethod
    def set_attribute(cls, element_name: str, attribute_name: str, attribute_value: str):
        return f'{element_name}.setAttribute("{underscore_to_hyphen(attribute_name)}", "{attribute_value}")'
    
    @classmethod
    def set_true(cls, element_name: str, argument: str):
        return f'{element_name}.{argument} = true'
    
    @classmethod
    def set_false(cls, element_name: str, argument: str):
        return f'{element_name}.{argument} = false'
    
    @classmethod
    def set_id(cls, element_name: str, element_id: str):
        return f'{element_name}.id = "{element_id}"'
    
    @classmethod
    def set_inner_text(cls, element_name: str, value: str):
        return f'{element_name}.innerText = "{value}"'
    
    @classmethod
    def set_inner_html(cls, element_name: str, value: str):
        return f'{element_name}.innerHTML = "{value}"'
    
    @classmethod
    def set_append_to(cls, element_name: str, *args):
        return f'{element_name}.append({join(args, sep=", ")})'
    
    @classmethod
    def set_prepend_to(cls, element_name: str, *args):
        return f'{element_name}.prepend({join(args, sep=", ")})'
    
    @classmethod
    def set_style(cls, element_name: str, attribute: str, value: str):
        return f'{element_name}.style.{attribute} = "{value}"'
    
    @classmethod
    def create_by_id(cls, element_id: str, tag: str):
        return join([cls.const_create_element(cls.camel_case(element_id), tag),
                     cls.set_id(cls.camel_case(element_id), element_id)], "; ")


class BaseStyle(UserString):
    @classmethod
    def root_item(cls, name: str, value: str):
        return f'--{name}: {value}'
    
    @classmethod
    def root(cls, *items: list[str]):
        return f':root {{{join(SmartList(*items), "; ")}}}'
    
    @classmethod
    def style_item(cls, name: str, value: str):
        return f'{name}: {value}'

    @classmethod
    def style_group(cls, *names, **items):
        return f'{join(SmartList(*names), ", ")} {{{join([f"{underscore_to_hyphen(k)}: {v}" for k, v in items.items()], "; ")}}}'
    
    @classmethod
    def inline_style(cls, *items: list[str]):
        return f'style="{join(SmartList(*items), "; ")}"'
    
    @classmethod
    def head_style(cls, roots: list[str] = None, items: list[str] = None):
        return f'<style>{cls.root(roots)} {join(items, " ")}"'



class BaseElement(UserString):
    """
    BaseElement(UserString):
    Base class for all html elements.
    :param *args: Tag, str and all BaseArgs, BaseScript and BaseElements
    :param before: BaseElement and str instances placed before self
    :param elements: BaseElement, Text and str instances placed inside self
    :param after: BaseElement and str instances placed after self
    :param style: StyleItem and str instances for inline style of self
    :param klass: Klass and str instances for class self definition
    :param script: BaseScript and str instances for script tag placed after before, self and after instances
    :param **kwargs: key value pairs for self config
    """
    TAG: Tag = None
    KLASS: str = None
    def __init__(self,
                 *args,
                 before: Optional[list[Union[BaseElement, str]]] = None,
                 elements: Optional[list[Union[BaseElement, Text, str]]] = None,
                 after: Optional[list[Union[BaseElement, str]]] = None,
                 style: Optional[Union[str, StyleItem]] = None,
                 klass: Optional[Union[str, Klass]] = None,
                 script: Optional[Union[str, BaseScript]] = None,
                 **kwargs
                 ):
        self.id = first_of_type(args, Id) or Id(kwargs.pop('id', None))
        self.name = first_of_type(args, Name) or Name(kwargs.pop('name', None))
        self.hx_config = first_of_type(args, HxConfig) or kwargs.get('hx_config', None)
        self.tag = first_of_type(args, Tag) or self.TAG or Tag(type(self).__name__.lower())
        self.args = [item for item in args if not isinstance(item, Tag)]
        self.klass = klass or self.KLASS
        self.elements = parse_list(elements)
        self.before = parse_list(before)
        self.after = parse_list(after)
        self.style = parse_list(style)
        self.script = parse_list(script)
        self.kwargs = kwargs
        super().__init__(str(self))

        
    def __str__(self):
        self.update()
        return self.data
        
    def update(self):
        self.data = remove_html_extra_whitespaces(self.render())
        
    @property
    def post_init_kwargs(self) -> dict:
        return {}
    
    @property
    def post_init_elements(self) -> list[BaseElement, str]:
        return []
    
    def from_args(self, tps: Union[type[GenericType], tuple[type[GenericType]]]) -> list[GenericType]:
        return list_of_type(self.args, tps)

        
    def render_kwargs(self):
        kwargs = set_filtered(SmartList(self.from_args(Kwarg), repr_dict(self.kwargs)))
        if len(kwargs) > 0:
            return f'{join(kwargs)}'
        return ''
    
    def render_klass(self):
        klass = set_filtered(SmartList(self.from_args(Klass), self.klass, self.KLASS))
        if len(klass) > 0:
            return f'class="{join(klass)}"'
        return ''
    
    def render_style(self):
        styles = set_filtered(SmartList(self.from_args(StyleItem), *self.style))
        if len(styles) > 0:
            return f'style="{join(styles, sep="; ")}"'
        return ''
    
    def render_after(self):
        return join(self.after)  # todo: if list_filtered(self.after) else ''
    
    def render_before(self):
        return join(self.before)  # todo: if list_filtered(self.before) else ''
    
    def render_elements(self):
        return join(SmartList(self.from_args((BaseElement, Text)), *self.elements))
    
    def render_args(self):
        return join(set_filtered(self.from_args((Arg, str))))
    
    def render_script(self):
        scripts = set_filtered(SmartList(self.from_args(BaseScript), *self.script))
        if scripts:
            return f'<script> {join(scripts, "; ")} </script>'
        return ''
    
    @property
    def config(self):
        return join([self.id, self.name, self.render_args(), self.render_klass(), self.render_kwargs(), self.hx_config, self.render_style()])
    
    def render(self):
        if self.tag.value in EMPTY_TAGS:
            return f'{self.render_before()}<{self.tag} {self.config}>{self.render_elements()}{join(self.render_after())}{self.render_script()}'
        return f'{self.render_before()}<{self.tag} {self.config}>{self.render_elements()}</{self.tag}>{self.render_after()}{self.render_script()}'
        
        
