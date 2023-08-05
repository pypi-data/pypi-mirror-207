import functools

from inverse.src.classes.abstract_data import DataAbstract
from inverse.src.classes.db_ops import DB_class_Opt
from inverse.src.engine.algos_save._save_sparse import algo_save_sparse_on_begin
from inverse.src.loggers._logger3 import get_my_logger
from inverse.src.utils.inverse_typings import *
from inverse.src.utils.partition import table_name_format

logging_ = get_my_logger('DBDataOpt')


class DBDataOpt(DataAbstract):
    buffer: dict = {}

    def __init__(self, threshold: int, name="test"):
        self.threshold = threshold
        self.name = name
        self.db_option = DB_class_Opt

    def key_format(self, r: int, name=False) -> str:
        if not name:
            name = self.name
        return f"{name}_{r}"

    @logging_
    def transpose_list(self, big_list: list_tuple, say: int) -> pddf:
        def get_name(index):
            return f"column_{self.threshold * (say) + index}"

        column_names = list(map(get_name, range(0, self.threshold)))

        df_t = pd.DataFrame(big_list).transpose()
        if len(df_t.columns) < self.threshold:
            column_names = column_names[0:  len(df_t.columns)]
        df_t.columns = column_names
        return df_t

    @logging_
    def save_part(self, say: int, big_list: list_tuple) -> None:
        self.db_option.write_db(table_name_format(self.name, say)
                                , self.transpose_list(big_list, say))

    @logging_
    def save_on_begin_rand(self, matrix: npar) -> None:
        from inverse.src.engine.algos_save._save_base import base_save_on_begin_rand
        return base_save_on_begin_rand(self, matrix)

    @logging_
    def save_sparse_on_begin(self, sparce_matrix, id_ekle_option=True) -> None:
        return algo_save_sparse_on_begin(self, sparce_matrix)


@logging_
def get_test_row(i):
    matrix = [[9, 17, 12], [2, 19, 12], [26, 8, 12]]
    return matrix[i]
