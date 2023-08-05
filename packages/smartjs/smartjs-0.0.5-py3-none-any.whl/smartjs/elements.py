__all__ = [
		'Div',
		'Span',
		'Ul',
		'Ol',
		'Li',
		'Input',
		'Textarea',
		'Select',
		'Option',
		'InstanceOption',
		'Head',
		'Meta',
		'Link',
		'Nav',
		'Body',
		'Header',
		'Footer',
		'Main',
		'ContainerFluid',
		'Container',
		'Heading',
		'NavLink',
		'NavItem',
		'ListGroup',
		'ListGroupItem',
		'Aside',
		'Anchor',
		'ListGroupItemAction',
		'BaseElement',
		'BaseArg',
		'Row',
		'Col',
		'HTML',
		'NavList'
]

from typing import Collection
from smartjs.base import *
from smartjs.functions import *
from smartjs.javascript import *


class Heading(BaseElement):
	def __init__(self, size: int, *args, **kwargs):
		self.size = size
		super().__init__(*args, **kwargs)
		
	@property
	def tag(self):
		return Tag(f'h{self.size}')


class Div(BaseElement):
	TAG = Tag('div')


class ContainerFluid(Div):
	KLASS = 'container-fluid'
	
	
class Container(Div):
	KLASS = 'container'
	
	
class Row(Div):
	KLASS = 'row'
	
	
class Col(Div):
	KLASS = 'col'
	
	
class Button(BaseElement):
	pass


class Span(BaseElement):
	pass




class Aside(BaseElement):
	pass


class Ul(BaseElement):
	pass


class Ol(BaseElement):
	pass


class Li(BaseElement):
	pass


class ListGroupItem(BaseElement):
	TAG = Tag('li')
	KLASS = 'list-group-item'
	

class ListGroup(BaseElement):
	TAG = Tag('ul')
	KLASS = 'list-group'
	

class ListGroupItemAction(BaseElement):
	TAG = Tag('a')
	KLASS = 'list-group-item-action'
	

class Anchor(BaseElement):
	TAG = Tag('a')
	
	
class NavList(BaseElement):
	TAG = Tag('ul')
	KLASS = 'nav'
	
	
class NavItem(BaseElement):
	TAG = Tag('li')
	KLASS = 'nav-item'
	
	
class NavLink(BaseElement):
	TAG = Tag('a')
	KLASS = 'nav-link'


class Input(BaseElement):
	def __init__(self, *args, _type: str = 'text', **kwargs):
		self.type = InputType(_type)
		super().__init__(*args, **kwargs)
		self.dict_kwargs['type'] = self.type.value
		
		
class Textarea(BaseElement):
	pass


class Select(BaseElement):
	pass


class Fieldset(BaseElement):
	pass


class Label(BaseElement):
	pass


class InputGroup(Div):
	KLASS = 'input-group'


class Form(BaseElement):
	KLASS = 'form-control'


class Option(BaseElement):
	pass

class BaseUniqueElement(BaseElement):
	@property
	def post_init_kwargs(self):
		return dict(id=type(self).__name__.lower())

class Main(BaseUniqueElement):
	pass



class Footer(BaseUniqueElement):
	pass


class Header(BaseUniqueElement):
	pass

class Nav(BaseElement):
	pass


class Title(BaseElement):
	def __init__(self, value: str):
		super().__init__(elements=[value])


class Head(BaseElement):
	def __init__(self, title: str, *args, **kwargs):
		self.head_title = title
		super().__init__(*args, **kwargs)
	
	@property
	def post_init_elements(self):
		return [
				Meta(charset='utf-8'),
				Meta(name="viewport", content="width=device-width, initial-scale=1"),
				Title(self.head_title),
				Link(
						href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css",
						rel="stylesheet",
						integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65",
						crossorigin="anonymous"
				),
				Script(src="/static/js/htmx.js")
		]


class Link(BaseElement):
	pass


class Meta(BaseElement):
	pass


class Body(BaseUniqueElement):
	def __init__(self, nav: Nav, main: Main, footer: Footer, **kwargs):
		self.nav = nav
		self.main = main
		self.footer = footer
		super().__init__(nav, main, footer, **kwargs)



class InstanceOption(BaseElement):
	TAG = Tag('option')
	def __init__(self, instance, *args, **kwargs):
		self.instance = instance
		super().__init__(*args, **kwargs)
		self.dict_kwargs['value'] = getattr(self.instance, "key", getattr(self.instance, "name"))
		self.dict_kwargs['id'] = f'{type(self.instance).__name__}.{getattr(self.instance, "key", getattr(self.instance, "name"))}'
		self.elements.append(str(self.instance))
		
	@classmethod
	def select_options(cls, items: Collection) -> str:
		return join(SmartList(Option(), [cls(item) for item in items]))
		

class HTML(BaseElement):
	def __init__(self, head: Head, body: Body):
		super().__init__(head, body)
		
	def render(self):
		return f'<!DOCTYPE html>{super().render()}'



if __name__ == '__main__':
	print(InstanceOption.select_options(InputType.__members__.values()))
	print(Meta(content="teste", name='viewport'))
	print(Link(rel="stylesheet", href="/style.css"))
	print(NavItem(NavLink(Text('home'), href="/")))
	print(Heading(1, Text('cabeçalho')))
	print(ContainerFluid(Text('teste')))
	print(Head())
	