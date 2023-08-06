__all__ = ['SmartPath', 'SmartQuery', 'CWDPath']

import datetime
import os
from typing import Union
from collections import UserDict
from pathlib import PurePath, Path
from urllib.parse import urlencode, urlsplit


class SmartQuery(UserDict):
    
    def url(self):
        return urlencode({k: v for k, v in self.data.items() if v})
    
    def with_contains(self, keys: list[str] = None):
        if keys:
            return {f'{k}?contains': str(v) for k, v in self.data.items() if v if k in keys}
        return {f'{k}?contains': str(v) for k, v in self.data.items() if v}
        


class SmartPath:
    def __init__(self, *args: Union[str, PurePath], **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.path = os.path.join(*args)
        self.query = urlencode(self.kwargs)

    def is_dir(self):
        return True if Path(self.path).is_dir() else False

    def parent(self):
        return Path(self.path).parent

    def directories(self):
        path = self.path if self.is_dir() else self.parent()
        return [i for i in Path(path).iterdir() if i.is_dir() if not i.parts[-1].startswith('.')]

    @property
    def url(self):
        if self.query:
            return '?'.join([str(self.path), self.query])
        return self.path
    
    
class CWDPath(SmartPath):
    def __init__(self, path: Union[str, PurePath]):
        super().__init__(Path(os.getcwd()), path)
        if not os.path.exists(self.url):
            super().__init__(Path(os.getcwd()).parent, path)
            if not os.path.exists(self.url):
                super().__init__(Path(os.getcwd()).parent.parent, path)
                if not os.path.exists(self.url):
                    super().__init__(Path(os.getcwd()).parent.parent.parent, path)
            

