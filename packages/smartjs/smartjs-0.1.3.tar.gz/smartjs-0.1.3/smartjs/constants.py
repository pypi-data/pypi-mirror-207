__all__ = ['GenericType', 'EMPTY_TAGS', 'FORM_FIELDS', 'TAGS','INPUT_TYPES', 'Number', 'YEAR_PATTERN', 'DAY_PATTERN',
           'MONTH_PATTERN', 'ISO_DATE_PATTERN', 'ISO_DATETIME_PATTERN', 'STRUCTURE', 'SEMANTIC']

import re
from typing import TypeVar
from decimal import Decimal


GenericType = TypeVar('GenericType')
Number = TypeVar('Number', float, int, Decimal)


EMPTY_TAGS: list[str] = ['input', 'img', 'meta', 'link', 'br', 'hr']
STRUCTURE: list[str] = ['html', 'head', 'body', 'title']
SEMANTIC: list[str] = ['header', 'footer', 'main', 'aside', 'nav']
FORM_FIELDS: list[str] = ['input', 'select', 'textarea']


TAGS: list[str] = [
		'a', 'address', 'area', 'abbr', 'article', 'aside', 'audio', 'body',
		'b', 'engine', 'bdi', 'bdo', 'blockquote', 'br', 'button', 'canvas', 'caption', 'cite', 'code', 'col',
		'colgroup', 'data', 'datalist', 'dd', 'del', 'details', 'dfn', 'div', 'dialog', 'dl', 'dt', 'em', 'embed',
		'fieldset', 'figcaption', 'figure', 'footer', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header',
		'hr', 'html', 'i', 'iframe', 'img', 'input', 'ins', 'kbd', 'label', 'legend', 'li', 'link', 'main', 'map',
		'mark', 'meta', 'meter', 'nav', 'nonscript', 'object', 'ol', 'optgroup', 'output', 'p', 'param', 'picture',
		'pre', 'progress', 'q', 'rp', 'rt', 'ruby', 's', 'samp', 'script', 'section', 'select', 'small', 'source',
		'span', 'strong', 'style', 'sub', 'summary', 'sup', 'svg', 'table', 'tbody', 'td', 'template', 'textarea',
		'tfoot', 'th', 'thead', 'time', 'title', 'tr', 'track', 'u', 'ul', 'var', 'video', 'wbr', 'option'
]

INPUT_TYPES: list[str] = [
		'button', 'checkbox', 'color', 'date', 'datetime-local', 'email', 'file', 'hidden', 'image', 'month',
		'number', 'password', 'radio', 'range', 'reset', 'search', 'submit', 'tel', 'text', 'time', 'url', 'week'
]


YEAR_PATTERN = re.compile(r'\b(19|20)\d{2}\b')

DAY_PATTERN = re.compile(r'\b([0-2]\d|3[0-1])\b')

MONTH_PATTERN = re.compile(r'\b(0\d|1[0-2])\b')

ISO_DATE_PATTERN = re.compile(r'(19|20)(\d{2})(-)(01|02|03|04|05|06|07|08|09|10|11|12)(-)([0-3]\d)')

ISO_DATETIME_PATTERN = re.compile(r'(19|20)(\d{2})(-)(01|02|03|04|05|06|07|08|09|10|11|12)(-)([0-3]\d)(T)([0-1]\d|2[0-3])(:)([0-5]\d)(?::[0-5]\d)?')



