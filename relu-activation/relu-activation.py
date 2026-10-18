import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    arr = np.array(x,dtype=float)
    return np.maximum(0,arr)