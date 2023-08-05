from abc import ABC

import scipy.sparse.linalg as splu
from scipy.sparse import eye
from scipy.sparse.linalg import (inv, spsolve)

from inverse.src.classes.random_sparse import get_random_sparse
from inverse.src.loggers._logger3 import get_my_logger, free_logger


# N = Bs.shape[0]
# iBs = inv(Bs)
# iBs = spsolve(Bs, eye(N))

class AlternativesInverse(ABC):
    """AlternativesInverse"""

    def __init__(self):
        # self.logger = logging.getLogger(self.__class__.__name__)
        name = self.__class__.__name__
        # print(name, " started  ...")
        self.logger = free_logger #  get_my_logger(name)  # set_logger(name, "AlternativesInverse.log")

        self.log(f"{name} started...")
        # self.warn(f"{name} started...")
        # self.log(f"{name} started...")

    # def warn(self, msg):
    #     self.logger.warning(msg)
    #     self.logger.info(msg)

    def log(self, msg):
        self.logger(msg)

    def log2(self, msg):
        self.logger(msg)


class SPLUInverse(AlternativesInverse):
    """SPLUInverse"""

    def inv(self, matrix):
        return splu.inv(matrix)


class BasicInverse(AlternativesInverse):
    """BasicInverse"""

    def inv(self, matrix):
        return inv(matrix)


class SPSolveInverse(AlternativesInverse):
    """SPSolveInverse"""

    def inv(self, matrix):
        return spsolve(matrix, eye(matrix.shape[0]))


def main_alternatives():
    matrix = get_random_sparse()
    alternatives = [SPLUInverse(), BasicInverse(), SPSolveInverse()]
    for alternative in alternatives:
        print(alternative.__class__.__name__)
        # print(alternative.inv(matrix))
        alternative.log(alternative.__class__.__name__)
        alternative.log(alternative.inv(matrix))


# main_alternatives
def help_alternatives():
    print('''
    from inverse.src.benchmarks.alternatives import SPLUInverse, SPSolveInverse, BasicInverse
    from inverse.src.benchmarks.alternatives import help_alternatives
    SPSolveInverse().inv( matrix )
    
    
    ''')
