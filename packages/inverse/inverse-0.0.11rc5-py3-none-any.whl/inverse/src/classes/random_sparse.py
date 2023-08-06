import numpy as np
from numpy.random import default_rng
from scipy import stats
from scipy.sparse import random
from scipy.stats import rv_continuous

from inverse.src.utils.pickle_works import sp_cache


class CustomDistribution(rv_continuous):
    def _rvs(self, size=None, random_state=None):
        return random_state.standard_normal(size)


rng = default_rng()


def get_random_sparse2():
    X = CustomDistribution(seed=rng)
    print(X)
    return X


@sp_cache
def get_random_sparse(m=30, n=None, density=0.25):
    if not n:
        n = m

    rng = default_rng()
    rvs = stats.poisson(25, loc=10).rvs
    S = random(m, n, density=density, random_state=rng, data_rvs=rvs)
    # print(type(S))
    # exit()
    # print(S.A)
    return S


def get_random_csc():
    from scipy.sparse import csc_matrix
    row = np.array([0, 0, 1, 1, 2, 1])
    col = np.array([0, 1, 2, 0, 2, 2])

    # taking data
    data = np.array([1, 4, 5, 8, 9, 6])

    # creating sparse matrix
    sparseMatrix = csc_matrix((data, (row, col)),
                              shape=(3, 3)).toarray()

    # # Creating a 3 * 4 sparse matrix
    # sparseMatrix = csc_matrix((30, 30),
    #                           dtype=np.int8).toarray()
    return sparseMatrix
