
import numpy as np

def disable_mul(fun):
    class array_no_mul(np.ndarray):
        def __mul__(self, other):
            raise RuntimeError('Multiplication has been disabled.')
    
    def wrapped(*args, **kwargs):
        M = fun(*args, **kwargs)
        return array_no_mul(M.shape, buffer=M, dtype=M.dtype)
    
    return wrapped

np.array = disable_mul(np.array)
