# from inverse import tic, toc

from rich.progress import Progress

from inverse.ctypes_loc.ctypes_class import c_divide, py_operate_inside_double
from inverse.src.engine.base_classes.big_matrix_base import BigMatrixAbstract
from inverse.src.utils.sure import tic, toc
from inverse.src.utils.tuple_for_buffer import get_tuple_for_buffer


def basic_algo(bg_matrix: BigMatrixAbstract):
    from inverse.src.utils.measure_calls import CallStack
    global CallStack
    tic()
    bucket = get_tuple_for_buffer(bg_matrix.n, bg_matrix.threshold)
    # exit()
    with Progress() as progress:
        task1 = progress.add_task("[red]Calculating...", total=len(bucket))
        for index, sira in enumerate(bucket):
            progress.update(task1, advance=1)
            CallStack["dis_dongu"] += 1
            sira = tuple(int(x) for x in \
                         sira if x < bg_matrix.n and x > -1)
            i, *y = sira
            sira_set = tuple(set(sira))
            bg_matrix.buffer.load_column_names_with_set(sira_set)
            row = tuple(bg_matrix.buffer.get_row(i))  # pivot = row[i]
            bg_matrix.buffer.set_row(i, c_divide(row, row[i]))  # SET Calculation

            # OBJECT = {bg_matrix: bg_matrix, i: i, j: j}

            items = ((bg_matrix, i, a) for a in tuple(set(y)) if a != i)
            # for j in items:
            _ = tuple(map(LONG_PROCESS, items))
            # with mp.Pool(4) as p:
            #     _ = p.map(LONG_PROCESS, items)

    bg_matrix.buffer.final_save()
    toc()
    inv_matrix = bg_matrix.buffer.get_current_matrix()
    bg_matrix.id_and_inv = inv_matrix
    print(CallStack)

    return inv_matrix[:, bg_matrix.n:]


def LONG_PROCESS(TUPLE):
    # print(TUPLE)
    bg_matrix, i, j = TUPLE

    CallStack["ic_dongu"] += 1
    row_J = tuple(bg_matrix.buffer.get_row(j))  # 3 array
    # number_j = row_J[i]
    if row_J[i] == 0:
        return
    row_i = tuple(bg_matrix.buffer.get_row(i))  # 4 array
    # number_i = row_i[i]
    nrow = py_operate_inside_double(
        row_J[i], row_i[i], row_J, row_i, len(row_J))
    # SET Calculation
    bg_matrix.buffer.set_row(j, nrow)


def basic_algo_sparse(bg_matrix: BigMatrixAbstract):
    from inverse.src.utils.measure_calls import CallStack
    global CallStack
    tic()
    bucket = get_tuple_for_buffer(bg_matrix.n, bg_matrix.threshold)

    if bg_matrix.test:
        print("Since bg_matrix.test was True, bucket was reduced to 5 element.")
        bucket = bucket[:5]
    # print(bucket)
    # exit()
    with Progress() as progress:
        task1 = progress.add_task("[red]Calculating inverse matrix ...", total=len(bucket))
        for index, sira in enumerate(bucket):
            progress.update(task1, advance=1)
            CallStack["dis_dongu"] += 1
            sira = tuple(int(x) for x in \
                         sira if x < bg_matrix.n and x > -1)
            i, *y = sira
            sira_set = tuple(set(sira))
            bg_matrix.buffer.load_column_names_with_set(sira_set)
            row = tuple(bg_matrix.buffer.get_row(i))  # pivot = row[i]
            bg_matrix.buffer.set_row(i, c_divide(row, row[i]))  # SET Calculation
            for j in (a for a in tuple(set(y)) if a != i):
                CallStack["ic_dongu"] += 1
                row_J = tuple(bg_matrix.buffer.get_row(j))  # 3 array
                number_j = row_J[i]
                if number_j == 0:
                    continue
                row_i = tuple(bg_matrix.buffer.get_row(i))  # 4 array
                number_i = row_i[i]
                nrow = py_operate_inside_double(
                    number_j, number_i, row_J, row_i, len(row_J))
                # SET Calculation
                bg_matrix.buffer.set_row(j, nrow)

    bg_matrix.buffer.final_save()
    toc()
    print("""
    Sparse Matrix inverse was calculated. 
    You may use get_row(name , index ) function to get row of inverse matrix. 
    
    """)

    # inv_matrix = bg_matrix.buffer.get_current_matrix()
    # bg_matrix.id_and_inv = inv_matrix

    # return inv_matrix[:, bg_matrix.n:]


def basic_algo_no_progress(bg_matrix: BigMatrixAbstract):
    from inverse.src.utils.measure_calls import CallStack
    global CallStack
    tic()
    bucket = get_tuple_for_buffer(bg_matrix.n, bg_matrix.threshold)
    print(bucket)
    # exit()
    for index, sira in enumerate(bucket):
        CallStack["dis_dongu"] += 1
        sira = tuple(int(x) for x in \
                     sira if x < bg_matrix.n and x > -1)
        i, *y = sira
        sira_set = tuple(set(sira))
        bg_matrix.buffer.load_column_names_with_set(sira_set)
        row = tuple(bg_matrix.buffer.get_row(i))  # pivot = row[i]
        bg_matrix.buffer.set_row(i, c_divide(row, row[i]))  # SET Calculation
        for j in (a for a in tuple(set(y)) if a != i):
            CallStack["ic_dongu"] += 1
            row_J = tuple(bg_matrix.buffer.get_row(j))  # 3 array
            number_j = row_J[i]
            if number_j == 0:
                continue
            row_i = tuple(bg_matrix.buffer.get_row(i))  # 4 array
            number_i = row_i[i]
            nrow = py_operate_inside_double(
                number_j, number_i, row_J, row_i, len(row_J))
            # SET Calculation
            bg_matrix.buffer.set_row(j, nrow)
    bg_matrix.buffer.final_save()
    toc()
    inv_matrix = bg_matrix.buffer.get_current_matrix()
    bg_matrix.id_and_inv = inv_matrix

    return inv_matrix[:, bg_matrix.n:]
