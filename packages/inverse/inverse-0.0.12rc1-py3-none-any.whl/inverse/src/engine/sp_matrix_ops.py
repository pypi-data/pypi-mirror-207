#   Sermet.Pekin 2023
#   matrix ops
#   bkz README.md.

from inverse.src.utils.pickle_file import save_pickle

from inverse.src.classes.randomMatrix import get_rand_matrix_int_seed

from inverse.src.utils.inverse_typings import *

# -----------------------------
#                   options
globalRow = 60
# -----------------------------
global_matrix = False


def nparray_to_df(array: npar) -> pddf:
    liste = []
    for x in array:
        y = list(x)
        liste.append(y)
    return pd.DataFrame(liste).transpose()


def ozet_show(items: list_tuple,
              limit=5, all=False) -> None:
    if len(items) < limit or all:
        a = items[:]
    else:
        a = items[0:limit]
    b = (str(round(x, 2)) for x in a if type(x) !=type(None )  )
    c = " ".join(b)
    if len(items) > limit:
        print(f"[{c}...]")
    else:
        print(f"[{c}]")


def display_matrix_ozet(matrix: npar,
                        name: str, limit=10) -> None:
    n = len(matrix)
    all = False
    print("=" * 100)
    print(" " * 20, name, " " * 20, f"{n}x{n} Matris")
    print("=" * 100)
    if n < limit:
        limit = n
        all = True
    for say in range(limit):
        ozet_show(matrix[say], limit, all)
    if n > limit:
        print("[...]")
    print("_" * 100)


def get_matrix_on_load() -> np.array:
    global global_matrix
    if isinstance(global_matrix, bool):
        # get_rand_matrix_int_seed(10)
        # get_rand_matrix_int_noseed(5)
        big_mat = get_rand_matrix_int_seed(globalRow)
        # big_mat = get_rand_matrix_int_noseed(globalRow)
        global_matrix = big_mat
        return big_mat
    return global_matrix


# --------------------------- Abstract ------------------
def save_on_begin(matrix: npar) -> None:
    n = len(matrix)
    for i in range(n):
        save_pickle("name" + str(i), matrix[i])


from inverse.ctypes_loc.ctypes_class import c_divide, c_multiply


def divide_pivot(row: list_tuple, pivot: int_float) -> tuple:
    if pivot == 0:
        raise ZeroDivisionError
    return c_divide(row, pivot)

    # print(pivot ,"pivot")
    assert isinstance(row, (tuple, list))
    assert isinstance(pivot, (int, float))
    row = np.array(row)
    if pivot != 0:
        # row = (x / pivot for x in row)
        row = row / pivot  # (x / pivot for x in row)
    else:
        raise ZeroDivisionError

    return tuple(row)


def divide_pivot_eski(row: list_tuple, pivot: int_float) -> tuple:
    assert isinstance(row, (tuple, list))
    assert isinstance(pivot, (int, float))
    row = np.array(row)
    if pivot != 0:
        # row = (x / pivot for x in row)
        row = row / pivot  # (x / pivot for x in row)
    else:
        raise ZeroDivisionError

    return tuple(row)

def combine_row_op(row_J: list_tuple,
                   row_i: list_tuple,
                   factor: int_float) -> list:
    row_J = np.array(row_J)
    row_i = np.array(row_i)

    return row_J - c_multiply(row_i, factor)


# @njit
def combine_row_op_eski(row_J: list_tuple,
                          row_i: list_tuple,
                          factor: int_float) -> list:
    row_J = np.array(row_J)
    row_i = np.array(row_i)
    return row_J - row_i * factor
    # result = []
    # for j_number, i_number in zip(row_J, row_i):
    #
    #     result.append(j_number - i_number * factor)
    # return result
