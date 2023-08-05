from inverse.ctypes_loc.ctypes_class import c_multiply, c_divide, py_operate_inside_double, \
    py_operate_inside_double_quick, py_equivalent_operate_inside_double


def test_baslik(capsys):
    with capsys.disabled():
        print("\n\n")
        print("=" * 50)
        print("=" * 10, " C TESTS ", "=" * 29)
        print("=" * 50)
        print("\n\n")


def test_c_multiply(capsys):
    ...
    with capsys.disabled():
        s1 = c_multiply([10, 20], 19)
        s2 = c_divide([10, 20], 1 / 19)
        print(s1)
        print(s2)
        assert s1 == s2 == [190, 380]


def test_py_operate_inside_double(capsys):
    with capsys.disabled():
        s1 = py_operate_inside_double(10, 20, [10, 20], [10, 20], 2)
        s2 = py_operate_inside_double_quick(10, 20, [10, 20], [10, 20], 2)
        print(s1)
        print(s2)
        s3 = py_equivalent_operate_inside_double(10, 20, [10, 20], [10, 20], 2)
        print(s3)

        # assert s1 == s2
        assert s3 == s1


def test_c_divide():
    ...


def test_c_add():
    ...


def test_c_subtract():
    ...


def test_free_memory():
    ...


def test_c_inverse():
    ...
