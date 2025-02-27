import numpy as np

def signoid (x) :
    return 1 /(1 + np.exp(-x))