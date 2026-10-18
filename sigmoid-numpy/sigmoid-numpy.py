import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    arr = np.asarray(x, dtype=float)
    out = np.empty_like(arr)

    pos = arr >= 0
    out[pos] = 1.0 / (1.0 + np.exp(-arr[pos]))

    e = np.exp(arr[~pos])
    out[~pos] = e / (1.0 + e)

    if np.isscalar(x) or arr.ndim == 0:
        return float(out)
    return out