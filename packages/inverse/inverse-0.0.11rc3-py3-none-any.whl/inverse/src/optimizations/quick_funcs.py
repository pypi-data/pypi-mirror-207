from inverse.src.engine.main_funcs_to_load import *
from inverse.src.utils.check_result import inverse_check

# cProfile.run('re.compile("foo|bar")', 'restats')
from auto_profiler import Profiler


def profile_this(f , *args  ) : 
    with Profiler():
        f(*args) 
        



def quick_sp_inverse(n = 100 ):
    print("testing...")
    threshold = n




    matrix = get_matrix_for_test(n)
    tic()
    display_matrix_ozet(matrix, "matrix ")

    converter = BigMatrixConverter("test")
    big_matrix = converter.convert_small_to_bigmatrix(matrix, threshold=threshold)  # class bigMatrix

    inv_big_matrix = big_matrix.sp_inverse()  # class bigMatrix
    # inv_big_matrix = big_matrix.sp_inverse_progress()  # class bigMatrix

    display_matrix_ozet(inv_big_matrix, "inverse matrix with inverse package ")

    toc()
    tic()

    matrix_check = inverse_check(matrix)
    display_matrix_ozet(matrix_check, "inv matris with numpy linalg")
    toc()