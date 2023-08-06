import numpy as np


def exp_normalize(x):
    b = x.max()
    y = np.exp(x - b)
    return y / y.sum()
