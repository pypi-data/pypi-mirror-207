from __future__ import annotations # Default behavior pending PEP 649

from collections.abc import Hashable
from typing import TypeVar, Generic, Any, NoReturn

# Immutable and hashable hash-map classes

A = TypeVar('A', bound=Hashable)
B = TypeVar('B', bound=Hashable)

class NamedFrozenSet(frozenset[A], Generic[A]):
    """Hashable and immutable named set."""
    
    __slots__ = ()
    
    def __repr__(self) -> str:
        
        name = type(self).__name__
        items = ''
        for i in self:
            if items == '':
                items += repr(i)
            else:
                items += (', ' + repr(i))
        
        return f'{name}({{{items}}})'

class NamedFrozenDict(dict[A, B], Generic[A, B]):
    """Hashable and immutable named mapping."""
    
    __slots__ = ()
    
    def __repr__(self) -> str:
        
        name = type(self).__name__
        
        return f'{name}({super().__repr__()})'
    
    def __hash__(self) -> int: # type: ignore
        
        return hash(frozenset(self.items()))
    
    def __ior__(self, *args: Any, **kwargs: Any) -> NoReturn: # type: ignore
    
        name = type(self).__name__
        msg = f"'{name}' object does not support dict union assignment"
        
        raise TypeError(msg)
    
    def __setitem__(self, *args: Any, **kwargs: Any) -> NoReturn:
        
        name = type(self).__name__
        msg = f"'{name}' object does not support item assignment"
        
        raise TypeError(msg)
    
    def __delitem__(self, *args: Any, **kwargs: Any) -> NoReturn:
        
        name = type(self).__name__
        msg = f"'{name}' object does not support item deletion"
        
        raise TypeError(msg)
    
    def clear(self, *args: Any, **kwargs: Any) -> NoReturn:
        
        name = type(self).__name__
        msg = f"'{name}' object does not support dict clear method"
        
        raise TypeError(msg)
    
    def pop(self, *args: Any, **kwargs: Any) -> NoReturn:
        
        name = type(self).__name__
        msg = f"'{name}' object does not support dict pop method"
        
        raise TypeError(msg)
    
    def popitem(self, *args: Any, **kwargs: Any) -> NoReturn:
        
        name = type(self).__name__
        msg = f"'{name}' object does not support dict popitem method"
        
        raise TypeError(msg)
    
    def update(self, *args: Any, **kwargs: Any) -> NoReturn:
        
        name = type(self).__name__
        msg = f"'{name}' object does not support dict update method"
        
        raise TypeError(msg)
    
    def setdefault(self, *args: Any, **kwargs: Any) -> NoReturn:
        
        name = type(self).__name__
        msg = f"'{name}' object does not support dict setdefault method"
        
        raise TypeError(msg)
