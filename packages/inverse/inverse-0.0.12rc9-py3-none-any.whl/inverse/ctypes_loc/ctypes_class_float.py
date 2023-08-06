# # pylint: disable=missing-class-docstring
# import ctypes
# from ctypes import *
# import numpy as np
# from pathlib import Path
#
# import os
#
#
# class CTypeConversion:
#     """"""
#
#     def __init__(self, name):
#         self.name = name
#         self.so_name = name + ".so"
#
#     def start(self, num=10):
#         path = Path(r"C:\Users\coldwater80\Desktop\PyCharmProjects\inversePackage\inverse\ctypes")  # os.getcwd()
#         self.clibrary = ctypes.CDLL(os.path.join(path, self.so_name))
#         clibrary = self.clibrary
#
#         values = (ctypes.c_float * 10)()
#         clibrary.multiplyVector.restype = ctypes.POINTER(ctypes.c_float)
#         clibrary.multiplyVector.argtypes = [
#             ctypes.POINTER(ctypes.c_float),
#             ctypes.c_int,
#             ctypes.c_float,
#         ]
#         self.free_memory_func = clibrary.free_memory
#
#     def free_memory(self, mult) -> None:
#         self.free_memory_func(mult)
#
#     def test_get_result(self, num=10) -> list:
#         return self.get_result(10, 2)
#
#     def get_result(self, num, multiplier) -> list:
#         values = (ctypes.c_float * num)()
#         for i in range(num):
#             values[i] = i
#
#         result_pointer = self.clibrary.multiplyVector(values, len(values), multiplier)
#         mylist = result_pointer[:num]
#         self.free_memory(result_pointer)
#
#
#         return mylist
#
#     def get_result_mult(self, array, multiplier) -> list:
#         num = len(array)
#         values = (ctypes.c_float * num)()
#         for i in range(num):
#             values[i] = array[i]
#
#         result_pointer = self.clibrary.multiplyVector(values, len(values), multiplier)
#         mylist = result_pointer[:num]
#         self.free_memory(result_pointer)
#
#
#         return mylist
#
#
# deneme_vector = CTypeConversion("vector_ops")
#
#
# def c_multiply(array, multiplier):
#     deneme_vector.start()
#     result = deneme_vector.get_result_mult(array, multiplier)
#
#     return result
#
#
# def c_divide(array, multiplier):
#     deneme_vector.start()
#     result = deneme_vector.get_result_mult(array, 1 / multiplier)
#
#     return result
#
#
# if __name__ == "__main__":
#     c_multiply([10, 20], 2)
#     c_divide([10, 20], 2)
#
# __all__ = ["c_multiply", "c_divide"]
