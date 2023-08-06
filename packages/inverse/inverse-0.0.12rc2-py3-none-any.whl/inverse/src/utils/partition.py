import math
from functools import lru_cache


def table_name_format(name, say):
    return f"{name}_{say}"


def table_name_format_reverse(name: str) -> int:
    return int(name.split("_")[-1])

@lru_cache(maxsize=128, typed=False)
def column_name_format(i):
    return f"column_{i}"

@lru_cache(maxsize=128, typed=False)
def get_table_name_treshold(i, treshold):
    i = int(i)
    return math.floor(i / treshold)

@lru_cache(maxsize=128, typed=False)
def get_name_from_i(i, treshold):
    return str(math.floor(i / treshold)), str(i % treshold)
