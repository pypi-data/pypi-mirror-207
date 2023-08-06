import timeit

from inverse.ctypes_loc.ctypes_class import c_multiply

number = 10_000_000

def test_c_multiply():
    array = tuple(x for x in range(number))
    multiplier = 2
    result = c_multiply(array, multiplier)
    # print(result)


def test_normal_multiply():
    array = list(x for x in range(number))
    for i in range(len(array)):
        array[i] = array[i] * 2
    # print(array)


start_time = timeit.default_timer()
test_normal_multiply()
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
test_c_multiply()
print(timeit.default_timer() - start_time)
