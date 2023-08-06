import ctypes
from ctypes import *
import numpy as np
from pathlib import Path


import os

path = os.getcwd()
clibrary = ctypes.CDLL(os.path.join(path, "vector_ops.so"))
values = (ctypes.c_float * 10)()
clibrary.multiplyVector.restype = ctypes.POINTER(ctypes.c_float)
clibrary.multiplyVector.argtypes = [
    ctypes.POINTER(ctypes.c_float),
    ctypes.c_int,
    ctypes.c_float,
]
free_memory = clibrary.free_memory

for i in range(10):
    #print("assigning", i)
    values[i] = i

mult = clibrary.multiplyVector(values, len(values), 2)
#print(mult)


mylist = mult[:10]

print(mylist)

# free_memory
free_memory(mult)
