import numpy as np

def iloczyn_skalarny_numpy(x, y):
    return np.dot(x, y)

a = np.arange(5)
b = np.arange(5)

print("Iloczyn skalarny (NumPy):", iloczyn_skalarny_numpy(a, b))