from inverse.src.classes.buffer_ops import get_table_names_from_tuple
from inverse.src.utils.partition import get_table_name_treshold
from inverse.src.utils.sp_utils_inverse import close_two_matrices, close_identity
from inverse.src.utils.tuple_for_buffer import get_tuple_for_buffer
from inverse.tests.tdisplay import tdisplay


# pytest ./tests/test_main.py -W ignore::DeprecationWarning -v

# pytest -W ignore::DeprecationWarning

# def test_inverse_random_matrix(capsys):
#    with capsys.disabled():
#        inverse_random_matrix(5, 50)
#       inverse_random_matrix(4, 12)


def test_together(capsys):
    with capsys.disabled():
        def a2(n=50):
            from inverse.src.engine.nontest_test import sp_inverse_t1, sp_inverse_mappings_t1
            a1 = sp_inverse_t1(n, silent=True)
            a2 = sp_inverse_mappings_t1(n, silent=True)

            tdisplay("test_together")
            print(a1)
            print(a2)
            assert a1 == a2

        a2(50)


def test_mini_tests(capsys):
    with capsys.disabled():
        tdisplay("MINI TESTS")


def gelen_kontrol(gelen):
    for items in gelen:
        x, *y = items
        y2 = list(y)
        y2.sort()
        print(y2)
        print(y)
        if tuple(y2) == tuple(y):
            pass
        else:
            return False
        return True


def test_gelen_kontrol():
    assert gelen_kontrol([[14, 23, 24, 25]]) == True
    assert gelen_kontrol([[14, 23, 2, 25]]) == False


def test_get_tuple_for_buffer(capsys):
    with capsys.disabled():
        a = get_tuple_for_buffer(5, 50)
        b = get_tuple_for_buffer(4, 12)
        assert gelen_kontrol(a) == True
        assert gelen_kontrol(b) == True

        print(a)
        print(b)


def test_get_table_name_treshold(capsys):
    items = [(15, 50), (20, 3), (16, 12)]

    with capsys.disabled():
        print("\ntest_get_table_name_treshold\n")
        for item, threshold in items:
            _ = get_table_name_treshold(item, threshold)
            print("item: ", item, "threshold: ", threshold, "result: ", _)


def test_get_table_name_treshold_adv(capsys):
    items = [x for x in range(25)]
    threshold = 5

    with capsys.disabled():
        print("\ntest_get_table_name_treshold\n")
        for item in items:
            _ = get_table_name_treshold(item, threshold)
            print("item: ", item, "threshold: ", threshold, "result: ", _)


def test_get_table_names_from_tuple(capsys):
    with capsys.disabled():
        items = [(14, 23, 24, 25), (14, 23, 24, 25)]

        def f(items_):
            return get_table_names_from_tuple(items_, 2)

        _ = tuple(map(f, items))
        print(_)


def test_get_table_names_from_tuple_basic(capsys):
    with capsys.disabled():
        items = (1, 180, 24, 25, 450)
        _ = get_table_names_from_tuple(items, 2)

        print(_)


def test_convert_small_to_bigmatrix():
    ...


def test_close_identity():
    eps = 0.05
    sonuc1 = [[1.001, 0, 0], [0, 1.001, 0], [0, 0, 1.001]]

    result = close_identity(matrix=sonuc1, eps=eps)
    assert result == True


def test_inverse_check():
    ...


# def test_sp_inverse_check():
#
#     from inverse.src.engine.nontest_test import sp_inverse_t1 , sp_inverse_mappings_t1
#     a1 = sp_inverse_t1()
#     a2 = sp_inverse_mappings_t1()
#     assert a1 == a2


def test_close_two_matrix(capsys):
    with capsys.disabled():
        print("\ntest_close_two_matrix\n")
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b = [[1.001, 2, 3], [4, 5, 6], [7, 8, 9]]

        result = close_two_matrices(a, b, 0.05)
        assert result == True
        print(result)
