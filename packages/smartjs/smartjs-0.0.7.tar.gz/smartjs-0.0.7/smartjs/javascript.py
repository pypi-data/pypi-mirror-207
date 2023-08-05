__all__ = [
        'ScriptStatement', 'ScriptFunction', 'ScriptConstant',  'ScriptVariable', 'ScriptListLoop',
        'ScriptEventListener', 'Script', 'ScriptJoin', 'ScriptInterval', 'ScriptCondition',
        'ScriptElse', 'ScriptIf', 'ScriptElseIf', 'ScriptTimeout',
        'ScriptAnonymous', 'BaseScript', 'ScriptById'
    ]

from typing import Union, Optional
from smartjs.functions import *
from smartjs.base import *


class ScriptStatement(BaseScript):
    def __init__(self, statement: str):
        self.statement = statement
        super().__init__(str(self.statement))


class ScriptJoin(BaseScript):
    def __init__(self, *args):
        self.args = args
        super().__init__(join(SmartList(*self.args), '; '))


class ScriptConstant(BaseScript):
    def __init__(self, name: str, statement: Union[str, ScriptStatement]):
        self.name = name
        self.statement = statement
        super().__init__(self.const(self.name, str(self.statement)))


class ScriptVariable(BaseScript):
    def __init__(self, name: str, statement: Union[str, ScriptStatement]):
        self.name = name
        self.statement = statement
        super().__init__(self.let(self.name, str(self.statement)))


class ScriptIf(BaseScript):
    def __init__(self, condition: str, statements: list[str]):
        self.condition = condition
        self.statements = statements
        super().__init__(self.if_statement(self.condition, self.statements))
        
        
class ScriptElseIf(BaseScript):
    def __init__(self, condition: str, statements: list[str]):
        self.condition = condition
        self.statements = statements
        super().__init__(self.else_if_statement(self.condition, self.statements))
        
        
class ScriptElse(BaseScript):
    def __init__(self, statements: list[str]):
        self.statements = statements
        super().__init__(self.else_statement(self.statements))
        
        
class ScriptCondition(BaseScript):
    def __init__(self, *args):
        self.if_clause = list_of_type(args, ScriptIf)
        self.else_if_clauses = list_of_type(args, ScriptElseIf)
        self.else_clause = list_of_type(args, ScriptElse)
        super().__init__(join([*self.if_clause, *self.else_if_clauses, *self.else_clause]))
        

class ScriptFunction(BaseScript):
    def __init__(self, name: str, arguments: str = '', statements: list[Union[str, ScriptStatement]] = None):
        self.name = name
        self.arguments = arguments
        self.statements = statements
        super().__init__(self.function(self.name, self.arguments, self.statements))


class ScriptAnonymous(BaseScript):
    def __init__(self, arguments: str = '', statements: list[Union[str, ScriptStatement]] = None):
        self.arguments = arguments
        self.statements = statements
        super().__init__(self.anonymous(self.arguments, self.statements))


class ScriptListLoop(BaseScript):
    def __init__(self, list_name: str, statements: list[Union[str, ScriptStatement]]):
        self.list_name = list_name
        self.statements = statements
        super().__init__(f'for (let i = 0; i < {self.list_name}.length; i++) {{{ScriptJoin(self.statements)}}}')


class ScriptEventListener(BaseScript):
    def __init__(self, const_or_var: str, event_name: str, function: Union[str, ScriptFunction]):
        self.const_or_var = const_or_var
        self.event_name = event_name
        self.function = function
        super().__init__(f'{self.const_or_var}.addEventListener("{self.event_name}", {str(self.function)})')


class ScriptInterval(BaseScript):
    def __init__(self, call: str, interval: int = 1000):
        self.call = call
        self.interval = interval
        super().__init__(f'setInterval({self.call}, {self.interval})')


class ScriptTimeout(BaseScript):
    def __init__(self, call: str, interval: int = 1000):
        self.call = call
        self.interval = interval
        super().__init__(f'setTimeout({self.call}, {self.interval})')


class ScriptFormField(BaseScript):
    def __init__(self, name: str, field_type: str, *args, **kwargs):
        self.name = name
        self.field_id = self.name
        self.field_tag = field_type.split(":")[0]
        if self.field_tag == "input":
            self.input_type = field_type.split(":")[-1]
        else:
            self.input_type = None
        self.is_hidden = True if self.input_type == 'hidden' else False
        self.is_checkbox = True if self.input_type == 'checkbox' else False
        self.field_class = 'form-check-input' if self.is_checkbox else 'form-control'
        self.container_class = 'form-check' if self.is_checkbox else 'form-floating'
        self.label_class = 'form-check-label' if self.is_checkbox else 'form-label'
        self.label_text = kwargs.pop('label', self.name)
        self.label_id = f'{self.name}__label'
        self.field_name = f'{self.camel_case(self.name)}'
        self.label_name = f'{self.field_name}Label'
        self.container_name = f'{self.field_name}Container'
        self.container_id = f'{self.name}__container'
        self.args = list_filtered(args)
        kwargs.update({'name': self.name, 'type': self.input_type})
        self.kwargs = dict_filtered(kwargs)
        super().__init__(self.render())
        
    def render(self):
        return ScriptJoin(
                self.element_field,
                self.element_label,
                self.element_container,
                self.append_to_container
        )
    
    @property
    def element_label(self):
        if not self.is_hidden:
            return ScriptJoin(
                    self.const_create_element(self.label_name, 'label'),
                    self.class_name(self.label_name, self.label_class),
                    self.set_attribute(self.label_name, 'for', self.name),
                    self.set_id(self.label_name, self.field_id),
                    self.set_inner_text(self.label_name, self.label_text)
            )
        return ''
    
    @property
    def element_field(self):
        return ScriptJoin(
                self.const_create_element(self.field_name, self.field_tag),
                self.class_name(self.field_name, self.field_class),
                *[self.set_attribute(self.field_name, k, v) for k, v in self.kwargs.items()],
                *[self.set_true(self.field_name, item) for item in self.args],
                self.set_id(self.field_name, self.name)
        )
    
    @property
    def element_container(self):
        return ScriptJoin(
                self.const_create_element(self.container_name, 'div'),
                self.class_name(self.container_name, self.container_class),
                self.set_id(self.container_name, self.container_id)
        )
    
    @property
    def append_to_container(self):
        if self.is_checkbox:
            return ScriptStatement(f'{self.container_name}.append({self.label_name}, {self.field_name})')
        elif self.is_hidden:
            return ScriptStatement(f'{self.container_name}.append({self.field_name})')
        else:
            return ScriptStatement(f'{self.container_name}.append({self.field_name}, {self.label_name})')


class ScriptForm(BaseScript):
    def __init__(self, id: str, action: str, method: str = 'post', form_class: str = 'form-control', form_fields: list[ScriptFormField] = None, **kwargs):
        self.id = id
        self.form_name = self.camel_case(self.id)
        self.action = action
        self.method = method
        self.form_class = form_class
        self.form_fields = form_fields
        self.kwargs = dict_filtered(kwargs)
        self.button_id = f'{self.id}__button'
        self.button_name = self.camel_case(self.button_id)
        super().__init__(self.render())
        
    def render(self):
        return ScriptJoin(
                self.const_create_element(self.form_name, 'form'),
                self.set_attribute(self.form_name, 'action', self.action),
                self.set_attribute(self.form_name, 'method', self.method),
                self.class_name(self.form_name, self.form_class),
                *[self.set_attribute(self.form_name, k, v) for k, v in self.kwargs.items()],
                self.set_id(self.form_name, self.id),
                ScriptJoin(*self.form_fields),
                *[self.set_append_to(self.form_name, *[item.container_name for item in self.form_fields])],
                self.const_create_element(self.button_name, 'button'),
                self.set_id(self.button_name, self.button_id),
                self.set_append_to(self.form_name, self.button_name)
        )
    
    
class ScriptById(BaseScript):
    def __init__(self, element_id: str):
        self.id = element_id
        self.name = self.camel_case(element_id)
        self.args = []
        self.instances = []
        self.data = repr(self)
        super().__init__(self.data)
        
    def __repr__(self):
        return f'{type(self).__name__}("{self.id}")'

    def __str__(self):
        self.setup()
        return self.data

    def render(self):
        return join(self.args, "; ")

    def setup(self):
        self.data = self.render()
        
    def append_instance(self, instance: 'ScriptById'):
        self.instances.append(instance)
        self.args = [*self.args, *instance.args]
        self.append(instance.name)
        return self
        
    def tag(self, tag: str):
        self.args.append(self.create_by_id(self.id, tag))
        return self
    
    def id_as_name(self):
        self.args.append(self.set_attribute(self.name, 'name', self.id))
        return self
    
    def change_name(self, name: str):
        self.args.append(self.set_attribute(self.name, 'name', name))
        self.name = name
        return self
    
    def get_style(self, attribute: str):
        return f'{self.get_computed_style(self.name)}["{attribute}"]'
        
    def change_id(self, element_id: str):
        self.args.append(self.set_id(self.name, element_id))
        self.id = element_id
        return self
    
    def append(self, *args):
        self.args.append(self.set_append_to(self.name, *args))
        return self
    
    def append_to(self, element_name: str):
        self.args.append(self.set_append_to(element_name, self.name))
        return self
    
    def prepend_to(self, element_name: str):
        self.args.append(self.set_prepend_to(element_name, self.name))
        return self
    
    def prepend(self, *args):
        self.args.append(self.set_prepend_to(self.name, *args))
        return self
        
    def style(self, name: str, value: str):
        self.args.append(self.set_style(self.name, name, value))
        return self
    
    def inner_text(self, text: str):
        self.args.append(self.set_inner_text(self.name, text))
        return self
    
    def inner_html(self, html: str):
        self.args.append(self.set_inner_html(self.name, html))
        return self
        
    def class_name(self, class_name: str):
        self.args.append(self.set_class_name(self.name, class_name))
        return self
    
    def attribute(self, name: str, value: str):
        self.args.append(self.set_attribute(self.name, name, value))
        return self
    
    def true(self, argument: str):
        self.args.append(self.set_true(self.name, argument))
        return self
    
    def false(self, argument: str):
        self.args.append(self.set_false(self.name, argument))
        return self
    

class Script(BaseScript):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        super().__init__(f'<script {self.render_kwargs()}> {self.render_args()} </script>')
    
    def render_kwargs(self):
        return repr_dict(dict_filtered(self.kwargs), sep=" ")
    
    def render_args(self):
        return join(SmartList(*self.args), '; ')


    
    
