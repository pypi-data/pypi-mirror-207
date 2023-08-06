def show_on_load():
    indent = 5 * " "

    print("=" * 50)
    print("inverse package was loaded...")
    import time
    time.sleep(1)
    print(f"to see examples run : \n{indent}inverse.test_basic() or test_basic() \n{indent}test_all() ")
    time.sleep(1)

    print("=" * 50)
