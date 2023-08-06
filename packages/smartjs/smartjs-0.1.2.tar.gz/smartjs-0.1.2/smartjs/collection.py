__all__ = ['SmartSet', 'SmartList']

from collections import UserList, deque
from typing import Iterable


class SmartList(UserList):
    def __init__(self, *args):
        self.data = list()
        self.include(*args)
        super().__init__(self.data)
    
    def __call__(self, *args):
        self.include(*args)
    
    def include(self, *args):
        for item in args:
            if isinstance(item, (tuple, list, set, deque)):
                self.include(*item)
            else:
                self.data.append(item)
    
    def extend(self, other: Iterable) -> None:
        self.include(*other)
    
    def append(self, item) -> None:
        self.include(item)
        
    def generator(self):
        return (item for item in self.data)
    
    def __len__(self):
        return len(self.data)

    

class SmartSet(set):
    def __init__(self, *args):
        self.data = SmartList(*args)
        super().__init__(set(self.data))
    
    def __call__(self, *args):
        self.include(*args)
    
    def include(self, *args):
        for item in args:
            if isinstance(item, (tuple, list, set, deque)):
                self.include(*item)
            else:
                self.data.append(item)
        super().__init__(set(self.data))


