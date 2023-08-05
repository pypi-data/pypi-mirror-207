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
        'SmartSet'
]

from enum import Enum
from collections import UserList, UserString
from smartjs.constants import *
from smartjs.functions import *


class Tag(Enum):
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
    pass


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


class Arg(BaseArg):
    def __init__(self, *args):
        super().__init__(join(args, sep=" "))
        
        
class Kwarg(BaseArg):
    def __init__(self, *args):
        self.args = [*args]
        super().__init__(self.args[0] if len(self.args) == 1 else f'{underscore_to_hyphen(self.args[0])}="{self.args[1]}"')


class Klass(BaseArg):
    def __init__(self, *args):
        super().__init__(join(args, sep=" "))
        
        
class StyleItem(BaseArg):
    def __init__(self, *args):
        self.args = [*args]
        super().__init__(self.args[0] if len(self.args) == 1 else f'{underscore_to_hyphen(self.args[0])}: {self.args[1]}')

            
class Text(BaseArg):
    def __init__(self, *args):
        super().__init__(join(args))
        

class BaseElement(UserString):
    TAG: Tag = None
    KLASS: str = None
    def __init__(self, *args, **kwargs):
        tag = list_of_type(args, Tag) or kwargs.pop('tag', None)
        if tag:
            if isinstance(tag, str):
                tag = Tag(tag)
            elif isinstance(tag, list):
                tag = tag[0]
        self.tag = tag
        self.klass = SmartList(list_of_type(args, Klass), kwargs.pop('klass', None))
        if self.KLASS:
            self.klass =[*self.KLASS.split(), *self.klass]
        self.style = SmartList(list_of_type(args, StyleItem), kwargs.pop('style', None))
        self.elements = SmartList(list_of_type(args, (BaseElement, Text)), kwargs.pop('elements', []))
        self.after = SmartList(kwargs.pop('after', []))
        self.before = SmartList(kwargs.pop('before', []))
        self.list_kwargs = SmartList(list_of_type(args, Kwarg), kwargs.pop('kwargs', None))
        self.args = SmartList(list_of_type(args, Arg), kwargs.pop('args', None))
        self.script: SmartList[BaseScript, str] = SmartList(*kwargs.pop('script', list()))
        self.dict_kwargs = kwargs
        self.dict_kwargs.update({k:v for k, v in self.post_init_kwargs.items() if not k in self.dict_kwargs.keys()})
        self.elements.extend(self.post_init_elements)
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
    def post_init_elements(self) -> list['BaseElement', str]:
        return []
        
    def render_kwargs(self):
        return f'{join(set_filtered(self.list_kwargs))} {repr_dict(self.dict_kwargs)}'
    
    def render_klass(self):
        return f'class="{join(set_filtered(self.klass))}"' if list_filtered(self.klass) else ''
    
    def render_style(self):
        return f'style="{join(set_filtered(self.style), sep="; ")}"' if list_filtered(self.style) else ''
    
    def render_after(self):
        return join(self.after) if list_filtered(self.after) else ''
    
    def render_before(self):
        return join(self.before) if list_filtered(self.before) else ''
    
    def render_elements(self):
        return join(self.elements)
    
    def render_args(self):
        return join(set_filtered(self.args))
    
    def render_script(self):
        if self.script:
            return f'<script> {join(self.script, "; ")} </script>'
        return ''
    
    @property
    def computed_tag(self):
        return self.tag or self.TAG or Tag(type(self).__name__.lower())
    
    @property
    def config(self):
        return join([self.render_args(), self.render_klass(), self.render_kwargs(), self.render_style()])
    
    def render(self):
        if self.computed_tag.value in EMPTY_TAGS:
            return f'{self.render_before()}<{self.computed_tag} {self.config}>{self.render_elements()}{join(self.render_after())}{self.render_script()}'
        return f'{self.render_before()}<{self.computed_tag} {self.config}>{self.render_elements()}</{self.computed_tag}>{self.render_after()}{self.render_script()}'
        
        
class SmartList(UserList):
    def __init__(self, *args):
        self.data = list()
        self.include(*args)
        super().__init__(self.data)
    
    def __call__(self, *args):
        self.include(*args)
    
    def include(self, *args):
        for item in args:
            if isinstance(item, (tuple, list, set)):
                self.include(*item)
            else:
                self.data.append(item)


class SmartSet(set):
    def __init__(self, *args):
        self.data = SmartList(*args)
        super().__init__(set(self.data))

    def __call__(self, *args):
        self.include(*args)

    def include(self, *args):
        for item in args:
            if isinstance(item, (tuple, list, set)):
                self.include(*item)
            else:
                self.data.append(item)
        super().__init__(set(self.data))
        

    
    

    

    
