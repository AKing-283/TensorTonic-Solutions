
import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    alpha = 1.6733
    lam = 1.0507

    result = []

    for value in x:
        if value > 0:
            output = lam * value
        else:
            output = lam * alpha * (math.exp(value) - 1)

        result.append(round(output, 4))

    return result
