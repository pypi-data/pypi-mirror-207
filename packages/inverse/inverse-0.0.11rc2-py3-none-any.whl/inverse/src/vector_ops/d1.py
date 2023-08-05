import numpy as np
import scipy.sparse.linalg as sla
from scipy import sparse
from scipy.linalg import blas


def p(*args):
    print(*args)


def dene_blas():
    n = 4096
    A = np.array(np.random.randn(n, n), order='F')
    B = np.array(np.random.randn(n, n), order='F')

    C_np = A @ B  # numpy  C = A * B
    C_blas = blas.dgemm(1.0, A, B)  # BLAS C = A * B

    p(C_blas, C_np)
    nd = np.linalg.norm(C_np - C_blas)

    print(nd)
    C_np = np.matmul(A, B)
    print(C_np)


def get_dene_lU_Matrix(n):
    A = sparse.random(n, n, 0.01) + sparse.eye(n)
    # plt.spy(A)
    # plt.show()
    return A


def dene_LU(n=15):
    A = get_dene_lU_Matrix(n)
    # https://caam37830.github.io/book/02_linear_algebra/sparse_linalg.html

    ILUfact = sla.spilu(A)
    return ILUfact


def main(n=15):
    for i in range(n):
        if i % 1000 == 0:
            print(i)
        for k in range(n):
            ...


main(150_000)


def main2():
    d = dene_LU(100_000)

    # d = dene_LU(np.array([[1, 5, 9], [4, 5, 6], [7, 8, 12]]))
    p(d)
    # dene_blas()
