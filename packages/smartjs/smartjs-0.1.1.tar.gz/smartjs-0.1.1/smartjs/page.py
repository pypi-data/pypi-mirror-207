import os

from typing import Union, TypeVar
from smartjs.base import *
from smartjs.constants import *
from smartjs.functions import *
from smartjs.elements import *
from smartjs.style import *
from smartjs.javascript import *
from pathlib import PurePath, Path

PathString = TypeVar('PathString', PurePath, Path, str)
NavLinkData = tuple[PathString, str]
NavLinkDataList = list[NavLinkData]


def head_element(title: str):
    return Head(title=title)


def nav_link(link: NavLinkData) -> NavLink:
    return NavLink( href=link[0], elements=[link[1]])


def nav_item(element: Union[str, BaseElement]) -> NavItem:
    return NavItem(elements=element)


def nav_list(nav_links: list[NavLinkData]) -> NavList:
    return NavList(elements=[nav_item(nav_link(link=link)) for link in nav_links])


def nav_brand(brand_link: NavLinkData) -> NavLink:
    return NavLink(href=brand_link[0], elements=[brand_link[1]], klass='navbar-brand')


def major_nav(nav_links: NavLinkDataList, brand_link: NavLinkData = None) -> Nav:
    return Nav(elements=[ContainerFluid(elements=[nav_brand(brand_link), nav_list(nav_links)])])


def html_page(title: str, nav_links: NavLinkDataList, brand_link: NavLinkData = None) -> HTML:
    brand_link = brand_link or ('/', 'Essência Psiquiatria')
    head = Head(title=title)
    body = Body(major_nav(nav_links=nav_links, brand_link=brand_link), Main(), Footer())
    return HTML(head=head, body=body)


if __name__ == '__main__':
    print(html_page('Daniel', nav_links=[
            (PurePath('/register'), 'registro'),
            ('/login', 'login'),
            ('/logout', 'logout'),
            ('/logout', 'logout')
    ]))


