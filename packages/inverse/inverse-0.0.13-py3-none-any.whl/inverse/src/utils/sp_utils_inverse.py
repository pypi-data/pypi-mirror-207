#   Sermet.Pekin 2023
#   matrix ops
#   bkz README.md.
import random

import numpy as np

msg_correcto = "Correct, this is Identity matrix"
msg_not_correcto = "This is Identity matrix"


def key_format(r, name="name"):
    return f"{name}_{r}"


def find_primes(n):
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


def max_prime_less_than_n(n):
    return find_primes(n)[-1]


def get_test_some_zero_matrix(n, prime=191):
    if prime > n:
        prime = max_prime_less_than_n(n)
    from inverse.src.optimizations.optimizations_when import matrix_for_test_big, make_some_zero

    # matrix = matrix2()
    matrix = matrix_for_test_big(n)
    # matrix = np.array(matrix)
    matrix = make_some_zero(matrix, prime=prime)
    return matrix


def memory_test(n, row=10):
    # numbers = list(random.randint(0, 100) for _ in range(n))
    big_numbers = []
    for i in range(row):
        # numbers = list(round(random.uniform(0, 1000000), 2) for _ in range(n))
        numbers = list(random.randint(0, 1_000_000) for _ in range(n))
        print(len(numbers))
        big_numbers.append(numbers)
    print(len(big_numbers))
    b = np.array(big_numbers)
    return b


def close_enough(sayi, buna, eps):
    return abs(sayi - buna) < eps


def inverse(mat):
    from scipy import linalg
    return linalg.inv(mat, overwrite_a=True)
    # return np.linalg.inv(mat)


class NotIdentity(BaseException):
    """Not an Identity Matrix"""


def close_identity_optimized(n, eps, data_source):
    # aug_matrix = np.column_stack((matrix, np.identity(n)))
    for i in range(n):
        pivot = data_source.get_row(i)[i]
        if close_enough(pivot, 1, eps):
            # aug_matrix[i] = aug_matrix[i] / pivot
            ...
        else:
            raise NotIdentity
        for j in range(n):
            if i != j:
                number = data_source.get_row(i)[j]
                if close_enough(number, 0, eps):
                    ...
                else:
                    raise NotIdentity
    print(msg_correcto)
    return True


def not_raise(dont_raise):
    if dont_raise:
        print(msg_not_correcto)
        return True
    else:
        raise NotIdentity


def close_identity(matrix, eps=0.001):
    n = len(matrix)
    # aug_matrix = np.column_stack((matrix, np.identity(n)))
    for i in range(n):
        pivot = matrix[i][i]
        if close_enough(pivot, 1, eps):
            # aug_matrix[i] = aug_matrix[i] / pivot
            ...
        else:
            not_raise(True)
            return False
        for j in range(n):
            if i != j:
                number = matrix[i][j]
                if close_enough(number, 0, eps):
                    ...
                else:
                    not_raise(True)
                    return False
    print(msg_correcto)
    return True


def close_two_matrices(matrix1, matrix2, eps=1e-10):
    n = len(matrix1)
    for i in range(n):
        if close_enough(matrix1[i][i], matrix2[i][i], eps):
            ...
        else:
            not_raise(True)
            return False
        for j in range(n):
            if close_enough(matrix1[i][i], matrix2[i][i], eps):
                ...
            else:
                not_raise(True)
                return False
    print(msg_correcto)
    return True
