# from inverse import tic, toc
from rich.progress import Progress

from inverse.src.engine.base_classes.big_matrix_base import BigMatrixAbstract
from inverse.src.engine.sp_matrix_ops import divide_pivot, combine_row_op
from inverse.src.utils.measure_calls import CallStack
from inverse.src.utils.tuple_for_buffer import get_tuple_for_buffer


def basic_algo_progress(bg_matrix: BigMatrixAbstract):
    self = bg_matrix

    with Progress() as progress:
        bucket = get_tuple_for_buffer(self.n, self.threshold)
        task1 = progress.add_task("[red]Calculating inverse matrix ...", total=len(bucket))
        for sira in bucket:
            CallStack["dıs_dongu"] += 1
            progress.update(task1, advance=1)
            # sira = tuple(x for x in sira if x < self.n)
            sira = tuple(int(x) for x in sira if x < self.n and x > -1)
            x, *y = sira
            y = tuple(set(y))

            self.buffer.load_column_names_with_set(sira)
            print("now x ", x, sira)
            for i in [x]:

                row = tuple(self.buffer.get_row(i))
                pivot = row[i]

                print("Sıradaki satır numarası : ", i,
                      "pivot :  ", pivot, "row", row, "*" * 10)
                # exit()
                row = divide_pivot(row, pivot)
                self.buffer.set_row(i, row)
                for j in y:
                    if i != j:

                        CallStack["ic_dongu"] += 1

                        number_j = self.buffer.get_cell(j, i)
                        number_i = self.buffer.get_cell(i, i)
                        if number_i != 0:
                            factor = number_j / number_i
                        else:
                            factor = 0
                        row_J = self.buffer.get_row(j)
                        row_i = self.buffer.get_row(i)
                        nrow = combine_row_op(row_J, row_i, factor)
                        self.buffer.set_row(j, nrow)
                        # print("setting nrow " , nrow )
    self.buffer.final_save()
    inv_matrix = self.buffer.get_current_matrix()
    self.id_and_inv = inv_matrix
    # print(inv_matrix)
    # return inv_matrix[:, self.n:]
    return inv_matrix
