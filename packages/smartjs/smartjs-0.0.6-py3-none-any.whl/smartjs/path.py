__all__ = ['SmartPath']
import os
from typing import Union
from functools import reduce
from pathlib import PurePath, Path
from urllib.parse import urlencode


class SmartPath:
    def __init__(self, *args: Union[str, PurePath], **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.pure_path = PurePath(*args)
        self.query = urlencode(self.kwargs)
        self.curdir = Path('.')
        
    @property
    def subdiretories(self, path: str = '.'):
        return [i for i in Path(path).iterdir() if i.is_dir()]
    
    def url(self):
        return '?'.join([str(self.pure_path), self.query])
        

if __name__ == '__main__':
    x = SmartPath('../.env')
    print(os.path.exists(x.pure_path))
    print(x.query)
    
    print(os.path.commonpath(paths=['smart/.env']))
