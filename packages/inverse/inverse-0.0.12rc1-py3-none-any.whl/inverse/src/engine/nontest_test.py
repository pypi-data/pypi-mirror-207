import numpy as np

from inverse.src.engine.matrix_converters import convert_small_to_big
from inverse.src.engine.sp_matrix_ops import display_matrix_ozet
from inverse.src.optimizations.optimizations_when import (create_mapping)
from inverse.src.utils.sp_utils_inverse import get_test_some_zero_matrix, close_two_matrices


# close_identity = lambda matrix, eps: np.allclose(matrix, np.eye(matrix.shape[0]), atol=eps)
# close_two_matrix = lambda matrix1, matrix2, eps: np.allclose(matrix1, matrix2, atol=eps)


class MatrixOps:
    def __init__(self, name, matrix, inv_matrix, np_inv_matrix=None):
        self.name = name

        self.matrix = matrix
        self.inv_matrix = inv_matrix
        self.np_inv_matrix = np.linalg.inv(matrix) if np_inv_matrix is None else np_inv_matrix

    def __eq__(self, other):
        eps = 0.05
        return close_two_matrices(self.matrix, other.matrix, eps) \
            and close_two_matrices(self.inv_matrix, other.inv_matrix, eps) \
            and close_two_matrices(self.inv_matrix, self.np_inv_matrix, eps)

    def __str__(self):
        print("=" * 50)
        print(self.name)
        print("=" * 50)

        display_matrix_ozet(self.matrix, "{0}   {1}  ".format(self.name, 'matrix'))

        display_matrix_ozet(self.inv_matrix, "{0}   {1}  ".format(self.name, 'inv_matrix'))
        display_matrix_ozet(self.np_inv_matrix, "{0}   {1}  ".format(self.name, 'np_inv_matrix'))
        return ""
        # return f"matrix: {self.matrix} \n inv_matrix: {self.inv_matrix} \n np_inv_matrix: {self.np_inv_matrix} \n"


def sp_inverse_t1(n,   threshold = 50 ,  silent=False):
    matrix = get_test_some_zero_matrix(n, prime=191)

    bg = convert_small_to_big(matrix, 't2' , threshold=threshold)

    bg_inv_kontrol = bg.sp_inverse()
    if not silent:
        display_matrix_ozet(matrix, 'bg_inv_kontrol')
        display_matrix_ozet(bg_inv_kontrol, 'bg_inv_kontrol')

    return MatrixOps("sp_inverse_t1", matrix, bg_inv_kontrol)


def sp_inverse_mappings_t1(n, silent=False):
    matrix = get_test_some_zero_matrix(n, prime=191)
    bg = convert_small_to_big(matrix, 't3' , threshold=50 )
    mapping = create_mapping(matrix)
    # print(mapping)
    bg_inv = bg.sp_inverse_with_mappings(mapping)
    if not silent:
        display_matrix_ozet(matrix, 'matrix')
        display_matrix_ozet(bg_inv, 'bg_inv_kontrol')

    return MatrixOps("sp_inverse_mappings_t1", matrix, bg_inv)


def test_sp_inverse_check(n=50):
    # from inverse.src.engine.nontest_test import sp_inverse_t1, sp_inverse_mappings_t1
    a1 = sp_inverse_t1(n, silent=True)
    a2 = sp_inverse_mappings_t1(n, silent=True)

    print(a1)
    print(a2)
    assert a1 == a2


__all__ = [
    "sp_inverse_mappings_t1",
    "sp_inverse_mappings_t1"
]
