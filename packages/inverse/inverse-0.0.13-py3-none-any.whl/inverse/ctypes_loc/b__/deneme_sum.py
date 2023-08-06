import ctypes
import os

path = os.getcwd()
clibrary = ctypes.CDLL(os.path.join(path, 'sum.so'))
values = (ctypes.c_int * 10)()

free_memory_int = clibrary.free_memory_int

for i in range(len(values)):
    values[i] = i

sum = clibrary.sumArray(values, len(values))
print(sum)

clibrary.incArray.restype = ctypes.POINTER(ctypes.c_int)

inc_array = clibrary.incArray(values, len(values))
mylist = inc_array[:10 ]

print(mylist)

# free_memory
free_memory_int(inc_array)