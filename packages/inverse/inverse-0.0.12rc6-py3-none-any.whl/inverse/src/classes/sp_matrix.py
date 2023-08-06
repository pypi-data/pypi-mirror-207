from scipy.sparse._coo import coo_matrix


class SPMatrix:
    def __init__(self, csc_matrix_):
        self.matrix_csc = csc_matrix_
        self.matrix_coo = csc_matrix_
        if not isinstance(csc_matrix_, coo_matrix):
            self.matrix_coo = csc_matrix_.tocoo()

    def get_line(self, line_number):
        matrix_coo = self.matrix_coo
        sonuc_values = []
        locations = []
        for index, (i, j, v) in enumerate(zip(matrix_coo.row, matrix_coo.col, matrix_coo.data)):
            # print(f"{index}  ({i},{j}) :  {v}")
            if i == line_number:
                sonuc_values.append(v)
                locations.append(j)
            if index > line_number:
                continue
        return locations, sonuc_values
