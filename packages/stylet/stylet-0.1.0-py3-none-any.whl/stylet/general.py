from __future__ import annotations # Default behavior pending PEP 649

from typing import Hashable, Collection, TypeVar, Generic, Self, Any, Callable

import numpy as np
import numpy.typing as npt

DType = TypeVar('DType', bound=np.generic)
DDims = TypeVar('DDims', bound=tuple[Collection[Hashable], ...])

RFunc = Callable[[npt.NDArray[Any], int], npt.NDArray[Any]]

class T(Generic[DType, DDims]):
    """Statically-typed labeled-element tensor of any rank."""
    
    values: npt.NDArray[DType]
    labels: DDims
    
    def __init__(self,
                 obj: T[DType, DDims] | tuple[npt.NDArray[DType], DDims]):
        
        if isinstance(obj, T):
            values = obj.values
            labels = obj.labels
        else:
            values, labels = obj
        
        self.shape = tuple(len(ks) for ks in labels)
        self.dtype = values.dtype
        
        assert_equal_shape(values, self.shape) # Raises ValueError if failed
        assert_unique_axes(labels) # Raises ValueError if failed
        
        self.values = values
        self.labels = labels
        
        self.dims = {d: n for n, d in enumerate(type(ks) for ks in labels)}
        self.idx = tuple({k: n for n, k in enumerate(ks)} for ks in labels)
    
    def __getitem__(self: Self, labels: DDims) -> Self:
        """Return tensor of same dimension sliced by labels."""
        
        kss = type(self.labels)((self.labels[n] if len(ks) == 0 else ks
                                 for n, ks in enumerate(labels)))
        
        nss = tuple(np.array([i[k] for k in ks])
                    for i, ks in zip(self.idx, kss))
        
        return type(self)((self.values[np.ix_(*nss)], kss))
    
    def s(self: Self,
          axis: type,
          key: Hashable) -> T[DType, Any]:
        """Return tensor one dimension down selected on key."""
        
        d = self.dims[axis]
        
        nss: tuple[int | slice, ...]
        nss = tuple(self.idx[d][key] if n == d else slice(None)
                    for n, _ in enumerate(self.labels))
        
        vs = self.values[nss]
        
        kss = (ks for n, ks in enumerate(self.labels) if n != d)
        return type(self)((vs, type(self.labels)(kss)))
    
    def r(self: Self,
          axis: type,
          func: RFunc) -> T[DType, Any]:
        """Return tensor one dimension down reduced with function."""
        
        d = self.dims[axis]
        
        vs = func(self.values, d)
        
        kss = (ks for n, ks in enumerate(self.labels) if n != d)
        return type(self)((vs, type(self.labels)(kss)))

# Runtime checks

def assert_equal_shape(values: npt.NDArray[Any], shape: tuple[int, ...]):
    """Raise ValueError if shapes of values and labels are different."""
    
    if not values.shape == shape:
        raise ValueError(f'values have shape {values.shape}, ' +
                         f'labels have shape {shape}')

def assert_unique_axes(labels: tuple[Collection[Hashable], ...]):
    """Raise ValueError if any axis is not unique."""
    
    ts = []
    for l in labels:
        t = type(l)
        if t in ts:
            raise ValueError(f'{t} axis is included more than once')
        else:
            ts.append(t)
