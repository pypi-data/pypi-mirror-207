from abc import ABC

from typing import Any


class BigMatrixAbstract(ABC):
    def __init__(self, name: str, n: int, threshold: int):
        self.name = name
        self.n = n
        self.threshold = threshold
        self.buffer: Any
        # post init
        # self.buffer = Buffer(self)
        # self.db_rep = DBDataOpt(threshold=threshold, name=self.name)
