def get_line(name, t1):
    return "{}: {:.5f}".format( name , t1)


def show_timeit_results(name, r1, r2, test_name1, test_name2):
    print("=" * 50)
    print("Results for ", name)

    print("=" * 50)
    a1 = get_line(test_name1, r1)
    a2 = get_line(test_name2, r2)
    print(a1 )
    print(a2 )

    # print( get_line(r1) , get_line(r2) )
    print(get_line("r1 / r2  :  ", r1 / r2))
    print("=" * 50)
