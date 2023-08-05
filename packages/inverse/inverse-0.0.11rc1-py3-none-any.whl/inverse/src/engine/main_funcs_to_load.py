

from inverse.src.classes.randomMatrix import get_matrix_for_test
from inverse.src.engine.matrix_converters import BigMatrixConverter
from inverse.src.engine.sp_matrix_ops import display_matrix_ozet
from inverse.src.testing_utils.timeit_sp import show_timeit_results
from inverse.src.utils.opening_logo import show_on_load
from inverse.src.utils.sp_utils_inverse import close_identity
from inverse.src.utils.sure import tic, toc


def inverse_random_matrix(n=10, threshold=50):
    import numpy as np
    from inverse.src.utils.check_result import inverse_check

    matrix = get_matrix_for_test(n)
    print(matrix)
    matrix_check = inverse_check(matrix)
    converter = BigMatrixConverter("test")
    big_matrix = converter.convert_small_to_bigmatrix(matrix, threshold=threshold)  # class bigMatrix
    tic()
    inv_big_matrix = big_matrix.sp_inverse()  # class bigMatrix
    toc()
    display_matrix_ozet(inv_big_matrix, "inv_big_matrix")
    display_matrix_ozet(inv_big_matrix, "inv_big_matrix main")
    display_matrix_ozet(matrix_check, "matrix_check")
    sonuc = np.matmul(matrix, inv_big_matrix)
    sonuc2 = np.matmul(matrix, matrix_check)
    display_matrix_ozet(sonuc, "sonuc A * A(-1)")
    display_matrix_ozet(sonuc2, "sonuc2 matrix_check A * A(-1)")
    eps = 0.0001
    kontrol = close_identity(matrix=sonuc, eps=eps)
    kontrol2 = close_identity(matrix=sonuc2, eps=eps)


show_on_load()


def test_basic(n=50):
    import timeit
    print("testing ... ")
    import time
    time.sleep(2)

    cy = timeit.timeit(f'sp_inverse_t1({n})', setup='from inverse.src.engine.nontest_test import sp_inverse_t1',
                       number=1)
    py = timeit.timeit(f'sp_inverse_mappings_t1({n})',
                       setup='from inverse.src.engine.nontest_test import sp_inverse_mappings_t1', number=1)

    show_timeit_results("test basic", cy, py, "sp_inverse_t1", "sp_inverse_mappings_t1")


def test_only_mappings(n=50):
    import timeit
    print("testing ... ")
    import time
    time.sleep(2)

    cy = timeit.timeit(f'sp_inverse_mappings_t1({n * 2})',
                       setup='from inverse.src.engine.nontest_test import sp_inverse_mappings_t1',
                       number=1)
    py = timeit.timeit(f'sp_inverse_mappings_t1({n})',
                       setup='from inverse.src.engine.nontest_test import sp_inverse_mappings_t1', number=1)

    show_timeit_results("test basic", cy, py, f"sp_inverse_mappings_t1 {n}*2 ", f"sp_inverse_mappings_t1 {n}")


#import pytest


def test_all():
    import pytest
    # pytest inverse/tests/test_main.py -W ignore::DeprecationWarning -v
    retcode = pytest.main()
    print("retcode = ", retcode)
