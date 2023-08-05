# __all__ = ['SmartPath']
# import os
# from typing import Union
# from pathlib import PurePath, Path
# from urllib.parse import urlencode
#
#
# class SmartPath:
#     def __init__(self, *args: Union[str, PurePath], **kwargs):
#         self.args = args
#         self.kwargs = kwargs
#         self.path = os.path.join(*args)
#         self.query = urlencode(self.kwargs)
#
#     def is_dir(self):
#         return True if Path(self.path).is_dir() else False
#
#     def parent(self):
#         return Path(self.path).parent
#
#     def directories(self):
#         path = self.path if self.is_dir() else self.parent()
#         return [i for i in Path(path).iterdir() if i.is_dir() if not i.parts[-1].startswith('.')]
#
#     @property
#     def url(self):
#         if self.query:
#             return '?'.join([str(self.path), self.query])
#         return self.path
#
#
# if __name__ == '__main__':
#     x = SmartPath(os.getcwd(), '.env')
#     print(x.url)
#     print(x.directories())
#