import numpy as np

from inverse.src.utils.check_result import inverse_check
from inverse.src.engine.matrix_converters import BigMatrixConverter
from inverse.src.utils.sp_utils_inverse import close_identity

from inverse.src.utils.measure_calls import CallStack

def test_mini_tests( capsys):
    with capsys.disabled():
        print("\n\n")
        print("=" * 50)
        print( "=" * 10 , " MAIN TESTS " ,  "=" * 29)
        print("=" * 50)
        print("\n\n")

def test_main_load(capsys):
    with capsys.disabled():
        threshold = 500
        matrix = np.array([[19, 2, 3],
                           [8, 3, 6],
                           [7, 8, 15]])
        big_matrix = BigMatrixConverter("test").convert_small_to_bigmatrix(matrix, threshold)
        inverse_mat = big_matrix.sp_inverse()
        # inverse_mat2 = big_matrix.sp_inverse_progress()
        matrix_check = inverse_check(matrix)

        print(matrix, "matrix")
        print(inverse_mat, "inverse_mat")
        # print(inverse_mat2, "inverse_mat2")
        print(matrix_check, "matrix_check")

        sonuc1 = np.matmul(matrix, inverse_mat)
        # sonuc2 = np.matmul(matrix, inverse_mat2)
        sonuc3 = np.matmul(matrix, matrix_check)

        eps = 0.0001
        kontrol = close_identity(matrix=sonuc1, eps=eps)
        # kontrol2 = close_identity(matrix=sonuc2, eps=eps)
        kontrol2 = close_identity(matrix=sonuc3, eps=eps)
        print(CallStack)