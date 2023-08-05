# from inverse import tic, toc
from inverse.ctypes_loc.ctypes_class import py_operate_inside_double, c_divide
from inverse.src.engine.base_classes.big_matrix_base import BigMatrixAbstract
from inverse.src.utils.tuple_for_buffer import get_tuple_for_buffer
from ...classes.sp_matrix import SPMatrix

from inverse.src.engine.algos._vector_ops import mult

def basic_algo_spsparse(bg_matrix: BigMatrixAbstract, sp_matrix: SPMatrix):
    self = bg_matrix
    """TODO"""
    global CallStack
    from inverse import tic, toc

    tic()
    bucket = get_tuple_for_buffer(self.n, self.threshold)

    for index, sira in enumerate(bucket):
        # print(sira)
        # exit()
        CallStack["dis_dongu"] += 1
        sira = tuple(int(x) for x in sira if x < self.n and x > -1)
        i, *y = sira

        sira_set = tuple(set(sira))
        self.buffer.load_column_names_with_set(sira_set)

        row = tuple(self.buffer.get_row(i))
        # pivot = row[i]

        # SET Calculation
        self.buffer.set_row(i, c_divide(row, row[i]))
        mat_indexes, mat_vals = sp_matrix.get_line(i)
        for j in (a for a in tuple(set(y)) if a != i):

            if j not in mat_indexes:
                continue

            CallStack["ic_dongu"] += 1
            row_J = tuple(self.buffer.get_row(j))  # 3 array
            row_i = tuple(self.buffer.get_row(i))  # 4 array

            number_j = row_J[i]
            number_i = row_i[i]

            nrow = py_operate_inside_double(
                number_j, number_i, row_J, row_i, len(row_J))
            # nrow = py_operate_inside_double_opt(i, row_J, row_i, len(row_J))

            # SET Calculation

            self.buffer.set_row(j, nrow)

    self.buffer.final_save()
    toc()
    inv_matrix = self.buffer.get_current_matrix()
    self.id_and_inv = inv_matrix
    # print(inv_matrix)

    return inv_matrix[:, self.n:]
