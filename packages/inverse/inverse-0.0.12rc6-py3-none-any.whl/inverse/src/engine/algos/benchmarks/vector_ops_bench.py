# from inverse.ctypes_loc.ctypes_class import py_operate_inside_double
import numpy as np
from scipy.linalg import blas

from inverse.ctypes_loc.ctypes_class import py_operate_inside_double

n = 4096
A = np.array(np.random.randn(n, n), order='F')
B = np.array(np.random.randn(n, n), order='F')




def benchmark_py_operate_inside_double():
    number_j = 1.0
    number_i = 2.0
    row_J = A[1]  # [1.0, 2.0, 3.0]
    row_i = B[1]  # [1.0, 2.0, 3.0]

    nrow = py_operate_inside_double(
        number_j, number_i, row_J, row_i, len(row_J))

    # print(nrow)
    return nrow


def bench_numpy():
    return blas.dgemm(1.0, A, B)

    # C_np = A @ B  # numpy  C = A * B
    # C_blas = blas.dgemm(1.0, A, B)  # BLAS C = A * B
    # print(C_blas)
    # sonuc = np.linalg.norm(C_np - C_blas)
