from __future__ import annotations # Default behavior pending PEP 649

from typing import TypeVar, Generic, Collection, Hashable, Union, overload

import numpy as np
import numpy.typing as npt

from .general import T

DType = TypeVar('DType', bound=np.generic)
D1 = TypeVar('D1', bound=Collection[Hashable])
D2 = TypeVar('D2', bound=Collection[Hashable])
D3 = TypeVar('D3', bound=Collection[Hashable])
D4 = TypeVar('D4', bound=Collection[Hashable])
D5 = TypeVar('D5', bound=Collection[Hashable])

class T0(T[DType, tuple[()]],
         Generic[DType]):
    """Statically-typed labeled-element tensor of rank zero."""
    
    def __init__(self,
                 obj: Union[T[DType, tuple[()]],
                            tuple[npt.NDArray[DType],
                                  tuple[()]]],):
        
        super().__init__(obj)
    
    def s(self, axis: type[()], key: Hashable) -> T0[DType]:
        
        return T0(super().s(axis, key))

class T1(T[DType, tuple[D1]],
         Generic[DType, D1]):
    """Statically-typed labeled-element tensor of rank one."""
    
    def __init__(self,
                 obj: Union[T[DType, tuple[D1]],
                            tuple[npt.NDArray[DType],
                                  tuple[D1]]],):
        
        super().__init__(obj)
    
    def s(self, axis: type[D1], key: Hashable) -> T0[DType]:
        
        return T0(super().s(axis, key))

class T2(T[DType, tuple[D1, D2]],
         Generic[DType, D1, D2]):
    """Statically-typed labeled-element tensor of rank two."""
    
    def __init__(self,
                 obj: Union[T[DType, tuple[D1, D2]],
                            tuple[npt.NDArray[DType],
                                  tuple[D1, D2]]]):
        
        super().__init__(obj)
    
    @overload
    def s(self, axis: type[D1], key: Hashable) -> T1[DType, D2]: ...
    
    @overload
    def s(self, axis: type[D2], key: Hashable) -> T1[DType, D1]: ...
    
    def s(self, axis, key): return T1(super().s(axis, key))

class T3(T[DType, tuple[D1, D2, D3]],
         Generic[DType, D1, D2, D3]):
    """Statically-typed labeled-element tensor of rank three."""
    
    def __init__(self,
                 obj: Union[T[DType, tuple[D1, D2, D3]],
                            tuple[npt.NDArray[DType],
                                  tuple[D1, D2, D3]]]):
        
        super().__init__(obj)
    
    @overload
    def s(self, axis: type[D1], key: Hashable) -> T2[DType, D2, D3]: ...
    
    @overload
    def s(self, axis: type[D2], key: Hashable) -> T2[DType, D1, D3]: ...
    
    @overload
    def s(self, axis: type[D3], key: Hashable) -> T2[DType, D1, D2]: ...
    
    def s(self, axis, key): return T2(super().s(axis, key))

class T4(T[DType, tuple[D1, D2, D3, D4]],
         Generic[DType, D1, D2, D3, D4]):
    """Statically-typed labeled-element tensor of rank four."""
    
    def __init__(self,
                 obj: Union[T[DType, tuple[D1, D2, D3, D4]],
                            tuple[npt.NDArray[DType],
                                  tuple[D1, D2, D3, D4]]]):
        
        super().__init__(obj)
    
    @overload
    def s(self, axis: type[D1], key: Hashable) -> T3[DType, D2, D3, D4]: ...
    
    @overload
    def s(self, axis: type[D2], key: Hashable) -> T3[DType, D1, D3, D4]: ...
    
    @overload
    def s(self, axis: type[D3], key: Hashable) -> T3[DType, D1, D2, D4]: ...
    
    @overload
    def s(self, axis: type[D4], key: Hashable) -> T3[DType, D1, D2, D3]: ...
    
    def s(self, axis, key): return T3(super().s(axis, key))
    
class T5(T[DType, tuple[D1, D2, D3, D4, D5]],
         Generic[DType, D1, D2, D3, D4, D5]):
    """Statically-typed labeled-element tensor of rank five."""
    
    def __init__(self,
                 obj: Union[T[DType, tuple[D1, D2, D3, D4, D5]],
                            tuple[npt.NDArray[DType],
                                  tuple[D1, D2, D3, D4, D5]]]):
        
        super().__init__(obj)
    
    @overload
    def s(self, axis: type[D1], key: Hashable) -> T4[DType, D2, D3, D4, D5]: ...
    
    @overload
    def s(self, axis: type[D2], key: Hashable) -> T4[DType, D1, D3, D4, D5]: ...
    
    @overload
    def s(self, axis: type[D3], key: Hashable) -> T4[DType, D1, D2, D4, D5]: ...
    
    @overload
    def s(self, axis: type[D4], key: Hashable) -> T4[DType, D1, D2, D3, D5]: ...
    
    @overload
    def s(self, axis: type[D5], key: Hashable) -> T4[DType, D1, D2, D3, D4]: ...
    
    def s(self, axis, key): return T4(super().s(axis, key))
