import random

from inverse import inverse_random_matrix
from inverse.src.classes.abstract_data import id_ekle
from inverse.src.engine.sp_matrix_ops import save_pickle


def save_on_begin_rand(n):
    for i in range(n):
        numbers = list(random.randint(0, 100) for _ in range(n))
        numbers += id_ekle(i, n)
        print(numbers)
        save_pickle("name" + str(i), numbers)


def test_save_on_begin_rand():
    # save_on_begin_rand(10)
    print("test")


def test_main2():
    # test_siralar()
    ...


def test_inverse_random_matrix(capsys):
    with capsys.disabled():
        inverse_random_matrix(5, 50)
        inverse_random_matrix(4, 12)
