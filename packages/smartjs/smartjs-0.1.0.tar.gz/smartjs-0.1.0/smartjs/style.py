__all__ = [
        'Style',
        'StyleGroup',
        'StyleRoot',
        'StyleRootItem',
        'StyleItem',
        'BaseStyle'
]

from typing import Union
from smartjs.functions import *
from smartjs.base import BaseStyle, StyleItem, SmartList


class StyleRootItem(BaseStyle):
    def __init__(self, *args: Union[str, tuple[str]]):
        self.args = [*args]
        super().__init__(self.args[0] if len(self.args) == 1 else f'--{args[0]}: {args[1]}')


class StyleRoot(BaseStyle):
    def __init__(self, *args: Union[StyleRootItem, tuple[StyleRootItem]]):
        self.args = args
        super().__init__(f':root {{{join(self.args, sep="; ")}}}')


class StyleGroup(BaseStyle):
    def __init__(self, *args: Union[str, StyleItem, tuple[str, StyleItem]], items: list[str] = None):
        self.args = list_filtered(args, lambda x: not isinstance(x, StyleItem))
        self.items = SmartList(list_of_type(args, StyleItem), items)
        super().__init__(f'{join(self.args, sep=", ")} {{{join(self.items, sep="; ")}}}')


class Style(BaseStyle):
    def __init__(self, *args: Union[tuple[StyleRootItem, StyleGroup], StyleRootItem, StyleGroup]):
        self.root = SmartList(list_of_type(args, StyleRootItem))
        self.declarations = SmartList(list_of_type(args, StyleGroup))
        super().__init__(f'<style> {{{f"{StyleRoot(*self.root)} {join(self.declarations)}"}}} </style>')

