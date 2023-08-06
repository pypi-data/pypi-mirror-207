import numpy as np
from rich.progress import Progress
from scipy.sparse import csc_matrix

from inverse.src.classes.abstract_data import id_ekle, DataAbstract
from inverse.src.classes.random_sparse import get_random_sparse
from inverse.src.classes.sp_matrix import SPMatrix
from inverse.src.loggers._logger3 import get_my_logger

# from inverse.src.classes.db_ops import DB_class_Opt

save_sparse_logging = get_my_logger('save_sparse_logging')


def get_zeros_and_values(coords, values, n):
    values_ = []
    # [ 0 , 5 , 12 ] [ 1 , 2 , 3 ]
    for i in range(n):
        if i not in coords:
            values_.append(0)
        else:
            values_.append(values.pop())
    return values_


@save_sparse_logging
def algo_save_sparse_on_begin(self: DataAbstract, sparce_matrix: csc_matrix) -> None:
    """This Will get the sparse matrix and save it in the database"""
    print('here ', sparce_matrix)
    # exit()
    say = -1
    part_say = -1
    big_list = []

    n = sparce_matrix.shape[0]

    sp_matrix = SPMatrix(sparce_matrix)

    print('DB save started...')
    # exit()
    with Progress() as progress:
        # bucket = get_tuple_for_buffer(self.n, self.threshold)
        task1 = progress.add_task("[red]Writing to database...", total=n)

        for i in range(n):

            # print(i)
            progress.update(task1, advance=1)
            coords, values = sp_matrix.get_line(i)

            numbers = get_zeros_and_values(coords, values, n)
            numbers += tuple(id_ekle(i, n))
            if len(big_list) == self.threshold:
                say = 0
                part_say += 1
                self.save_part(part_say, big_list)
                big_list = [numbers]

            else:
                say += 1
                big_list.append(numbers)

        if big_list:
            part_say += 1
            # print('SAVING THIS ONE TOO', say, big_list)

            assert not (len(big_list) > self.threshold)

            self.save_part(part_say, big_list)


def t_save_sparse_on_begin(n, threshold, test=False):
    from inverse.src.engine.sp_matrix_ops import display_matrix_ozet
    from inverse import BigMatrixConverter
    matrix = get_random_sparse(m=n, n=n, density=0.25)
    sparce_matrix = csc_matrix(matrix)
    sp_mat = SPMatrix(sparce_matrix)

    big_matrix = BigMatrixConverter(
        "sparce_matrix_test").convert_sparse_to_bigmatrix(sparce_matrix, threshold)
    big_matrix.test = test
    inverse_mat = big_matrix.sp_inverse_with_spsparse(sp_mat)
    if isinstance(inverse_mat, np.ndarray or np.matrix):
        display_matrix_ozet(inverse_mat, "inverse_mat")


# ---------------------------------------------------------------

'''
def t_save_sparse_on_begin222(n=30, threshold=500, Test=False):
    # threshold = 500
    # matrix = np.array([[19, 2, 3, 8],
    #                    [8, 3, 6, 9],
    #                    [7, 8, 15, 11],
    #                    [4, 7, 8, 5]])

    matrix = get_random_sparse(m=n, n=n, density=0.25)

    # eye = np.eye(3, dtype=np.int64)
    # matrix = matrix + eye
    # print(matrix.shape, "matrix.shape")
    sparce_matrix = csc_matrix(matrix)

    # exit()

    big_matrix = BigMatrixConverter(
        "sparce_matrix_test").convert_sparse_to_bigmatrix(sparce_matrix, threshold)
    big_matrix.test = Test
    inverse_mat = big_matrix.sp_sparse_inverse()
    # inverse_mat = big_matrix.sp_inverse_progress()
    print(inverse_mat)
    return

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


def _aaa():
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
    


'''
