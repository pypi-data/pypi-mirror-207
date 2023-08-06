from functools import lru_cache

from inverse.src.utils.inverse_typings import *
from inverse.src.utils.measure_calls import CallStack
from inverse.src.utils.partition import get_table_name_treshold, table_name_format, column_name_format, \
    table_name_format_reverse
from .db_ops import DB_class_Opt
from ..loggers._logger3 import get_my_logger, free_logger

logging_ = get_my_logger('Buffer')


@lru_cache(maxsize=128, typed=False)
def get_table_names_from_tuple(liste: list_tuple, threshold: int) -> list_tuple:
    new_set = []
    for i in liste:
        num = get_table_name_treshold(i, threshold)
        if num not in new_set:
            new_set.append(num)
    return tuple(new_set)


class Buffer:
    def __init__(self, bigmatrix):
        self.buffer_data = {}
        self.bigmatrix = bigmatrix
        self.threshold = self.bigmatrix.threshold
        self.name = self.bigmatrix.name
        self.columns = []
        self.columns_tables_dict = {}

    def buffer_to_matrix(self) -> npar:
        def get(name: str):
            keyname = self.columns_tables_dict[name]
            # print("keyname : ", keyname)
            return self.buffer_data[keyname][name]

        keys = tuple(self.columns_tables_dict.keys())
        rows = (x for x in keys if x not in ("index", "level_0"))
        # print(tuple(rows))
        liste = tuple(map(get, rows))
        # liste = tuple(x for x in liste)
        # print(liste)

        # input("devam")

        return np.array(liste)

    def get_current_matrix(self) -> npar:
        n = self.bigmatrix.n

        new_set = get_table_names_from_tuple(tuple(x for x in range(n)), self.threshold)
        # new_set = get_tuple_for_buffer(n, self.threshold)[0]
        # print(self.buffer_data.keys())
        # input("here the buffer keys  ")
        self.load_buffer(new_set)
        matrix = self.buffer_to_matrix()
        return matrix

    def buffer_get_current_key_nums(self) -> tuple:

        return tuple(map(table_name_format_reverse, tuple(self.buffer_data.keys())))

    @lru_cache(maxsize=128, typed=False)
    def buffer_key_format(self, say: int) -> str:
        return table_name_format(self.name, say)

    @logging_
    def load_buffer(self, diff_set: list_tuple) -> None:
        """burada desteleri yükleyecek"""

        for set_say in diff_set:

            # print("loading ... ", set_say)
            table_name = table_name_format(self.name, set_say)
            buffer_key = self.buffer_key_format(set_say)
            try:
                df = DB_class_Opt.read_db(table_name)

                for column in tuple(df.columns):
                    self.columns_tables_dict[column] = buffer_key
                self.buffer_data[buffer_key] = df
            except Exception as exc:
                print(exc)
        # print(tuple(self.buffer_data.keys()))
        # input("checking buffer...")

    def save_buffer(self, diff_set=()) -> None:
        if not diff_set:
            diff_set = tuple(self.buffer_data.keys())

        for table_name in diff_set:
            try:
                DB_class_Opt.write_db(table_name, self.buffer_data[table_name])
            except:
                print("bunu bulamadım save_buffer ", table_name)

    @logging_
    def empty_buffer(self, tuple_set=()) -> None:
        if tuple_set:
            for item in tuple_set:
                try:
                    self.buffer_data.pop(item)
                except:
                    print('no key found buffer ops 104', item)
        else:
            self.buffer_data = {}

    @logging_
    def refresh_buffer(self, new_set: list_tuple, onload=False) -> None:

        old_set = self.buffer_get_current_key_nums()

        diff_set_garbage = tuple(x for x in old_set if x not in new_set)
        diff_set_load = tuple(x for x in new_set if x not in old_set)


        if onload or not old_set:
            return self.load_buffer(new_set)

        if self.threshold < len(tuple(self.buffer_data.keys())):
            ...
            # self.save_buffer(diff_set_garbage)
            # self.empty_buffer(diff_set_garbage)
        if diff_set_load:
            self.load_buffer(diff_set_load)

    @logging_
    def load_column_names_with_set_onload(self, column_tuple: list_tuple) -> None:
        CallStack["load_column_names_with_set_onload"] += 1

        new_set = get_table_names_from_tuple(tuple(set(column_tuple)), self.threshold)

        self.refresh_buffer(new_set, onload=True)

    @logging_
    def load_column_names_with_set(self, column_tuple: list_tuple) -> None:
        CallStack["load_column_names_with_set"] += 1

        column_tuple = tuple(set(column_tuple))

        # (0,)
        new_set = get_table_names_from_tuple(column_tuple, self.threshold)
        # print("load_column_names_with_set new_set", new_set)

        # print("load_column_names_with_set new_set", new_set)
        # exit()
        self.refresh_buffer(new_set)

    @logging_
    def setItem(self, num: int, i: int, data: list_tuple) -> None:
        buffer_key = self.buffer_key_format(num)
        df = self.buffer_data[buffer_key]
        keyname = column_name_format(i)
        df[keyname] = data
        self.buffer_data[buffer_key] = df

    @logging_
    def get_column(self, i: int) -> pddf:
        column = column_name_format(i)
        keyName = self.columns_tables_dict[column]
        return self.buffer_data[keyName]

    def get_cell(self, j: int, i: int) -> int_float:
        column = column_name_format(j)
        df = self.get_column(j)
        return tuple(df[column])[i]

    @logging_
    def get_row(self, i: int) -> tuple:
        column = column_name_format(i)

        # free_logger(f'{self.columns_tables_dict.keys()} ')
        try:
            keyName = self.columns_tables_dict[column]
        except:
            print(column, i, 'ERROR', tuple(self.columns_tables_dict.keys()))
            raise Exception

        return tuple(self.buffer_data[keyName][column])

    @logging_
    def set_row(self, i: int, data: list_tuple) -> None:
        num = get_table_name_treshold(i, self.threshold)
        self.setItem(num, i, data)

    @logging_
    def final_save(self) -> None:
        # print("final save operation")
        self.save_buffer()
        # self.buffer_data = {}
