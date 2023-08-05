import numpy as np


def test_some(capsys):
    with capsys.disabled():
        print("\n\n")
        print("=" * 50)
        print("=" * 10, " Some Matrices ", "=" * 29)
        print("=" * 50)
        print("\n\n")


def test_matrix1(capsys):

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
        [0.06, -0.07, -0.3, 0.42,  -0.23],
        [0.1, -0.12, -0.33, 0.45, -0.18],
        [0.05, -0.06, -0.18, 0.29, -0.16]
    ]

    a = np.array(a)
    a_inv = np.array(a_inv)
    calc_inv = np.linalg.inv(a)

    def equal(a, b, eps=0.01):
        n = a.shape[0]

        for i in range(n):
            for j in range(n):
                try:
                    ax = a[i][j]
                    bx = b[i][j]
                    fark = ax - bx
                    if abs(fark) < eps:
                        pass
                    else:
                        return False
                        ...

                except Exception as exc:
                    print('i....', i, a, exc)
        return True

    with capsys.disabled():

        assert equal(a_inv, calc_inv) == True
