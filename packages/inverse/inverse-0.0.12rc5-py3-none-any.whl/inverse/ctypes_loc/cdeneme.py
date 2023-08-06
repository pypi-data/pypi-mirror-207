# import os

# # from ctypes import py_object
# from ctypes import *
# from pathlib import Path
# import ctypes
# from inverse.ctypes_loc.get_c_loc import * 



# CDLL = cdll
# import numpy as np

# import ctypes
# from ctypes import *

# curr_dir = os.path.dirname(__file__)

# path = Path(curr_dir)  # os.getcwd()


# clibrary = get_c_lib( 'clib.c' )


# display = clibrary.display

# display.argtypes = [ctypes.c_char_p, ctypes.c_int]
# display.restype = ctypes.c_char_p


def test_c():
    ... 

    # gelen = display(b"sermet", 43)
    # print(bytes(gelen))


# # test_c()
#
#
# clibrary_vector = ctypes.CDLL(
#     r"C:\Users\coldwater80\Desktop\PyCharmProjects\inversePackage\inverse\ctypes\vector_ops.so")
#
# multiplyVector = clibrary_vector.multiplyVector
#
# multiplyVector.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.c_float]
# multiplyVector.restype = ctypes.POINTER(ctypes.c_float)
#
# free_func = clibrary_vector.free_memory
# free_func.argtypes = [ctypes.POINTER(ctypes.c_float)]
#
#
# def test_multiplyVector():
#     b = np.array([15, 1], dtype=np.int32)
#     a = b.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
#
#     gelen_pointer = multiplyVector(a, 2, 1)
#     print(gelen_pointer)
#     gelen_deger = ctypes.c_float.from_buffer(gelen_pointer)
#
#     free_func(gelen_pointer)
#     print(gelen_deger.value)
# # test_multiplyVector()
