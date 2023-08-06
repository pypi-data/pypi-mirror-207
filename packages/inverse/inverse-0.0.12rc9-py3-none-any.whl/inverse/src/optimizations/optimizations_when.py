from inverse.src.engine.main_funcs_to_load import *
import numpy as np

def deneme_matrix():
    matrix = [
        [0, 0, 20, 0, 18, 20, 0],
        [14, 18, 20, 12, 18, 20, 14],
        [9, 18, 20, 12, 18, 20, 14],
        [4, 18, 20, 12, 18, 20, 14],
        [7, 18, 20, 12, 18, 20, 14],
        [5, 0, 0, 8, 9, 20, 14],
        [0, 8, 0, 0, 9, 20, 14]
    ]
    matrix = get_matrix_for_test(3)

    return np.array(matrix)


def create_value_guide_for_matrix():
    liste = [(3, 5, 6), (2, 3, 4), (1, 2)]
    return liste


def some_zero(n=5):
    # a = create_value_guide_for_matrix()
    # a = deneme_matrix()
    # a = get_matrix_random(5)
    a = matrix1()
    b = np.linalg.inv(a)
    c = np.multiply(a, b)

    display_matrix_ozet(a, "a  ")
    display_matrix_ozet(b, "b  ")
    display_matrix_ozet(c, "c  ")


# some_zero()


def matrix1():
    a = [
        [49, 2, 49, 81, 36],
        [40, 57, 70, 78, 44],
        [17, 60, 8, 45, 82],
        [17, 81, 21, 57, 77],
        [11, 55, 17, 46, 32],
    ]

    a_inv = [
        [-0.24, 0.31, 0.96, -1.35, 0.63],
        [-0.08, 0.1, 0.28, -0.4, 0.2],
        [0.06, -0.07, -0.3, 0.42, -0.23],
        [0.1, -0.12, -0.33, 0.45, -0.18],
        [0.05, -0.06, -0.18, 0.29, -0.16]
    ]

    return np.array(a)


def try_mapping_big(x=10, asal=19):
    mappings = []
    for i in range(x):
        line = []
        for j in range(x):
            if (i + 1) * (j + 1) % asal == 0:
                print('.. ', i)
                line.append(j + 1)
        mappings.append(line)
    return mappings


def make_some_zero(matrix, prime=17):
    x = matrix.shape[0]

    for i in range(x):
        for j in range(x):
            if i != j:
                if (j * 10 + 1) % prime != 0:
                    matrix[i][j] = 0

    return matrix


def create_mapping(matrix=None):
    if isinstance(matrix, type(None)):
        matrix = matrix2()

    def close_zero(num, eps=0.00001):
        return abs(num) < eps

    n = matrix.shape[0]
    mappings = []

    for i in range(n):
        line = []
        for j in range(n):
            if not close_zero(matrix[i][j]):
                line.append(j + 1)
        mappings.append(line)
    return mappings


def matrix2():
    a = [
        [49, 2, 49, 81, 36],
        [0, 1, 70, 0, 44],
        [0, 0, 8, 0, 82],
        [0, 0, 21, 57, 0],
        [0, 55, 0, 46, 32],
    ]

    '''

    
    '''

    # check_inverse2

    return np.array(a)


def check_inverse(matrix=matrix1()):
    print(matrix)

    b = np.linalg.inv(matrix)
    print(b, '....b')
    c = np.dot(matrix, b)
    print(c, '....c')

    return close_identity(c, 0.05)


def matrix_for_test_big(n=100):
    matrix = get_matrix_for_test(n)
    return matrix


def check_inverse2():
    matrix = matrix2()

    b = np.linalg.inv(matrix)
    print(b, '....b')
    c = np.dot(matrix, b)
    print(c, '....c')

    return close_identity(c, 0.05)
