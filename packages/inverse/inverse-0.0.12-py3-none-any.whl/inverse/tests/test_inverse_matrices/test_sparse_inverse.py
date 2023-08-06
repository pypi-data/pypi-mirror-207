from inverse.src.engine.algos_save._save_sparse import t_save_sparse_on_begin


def test_some(capsys):
    with capsys.disabled():
        print("\n\n")
        print("=" * 50)
        print("=" * 10, " t_save_sparse_on_begin ", "=" * 29)
        print("=" * 50)
        print("\n\n")


def test_t_save_sparse_on_begin(capsys):
    t_save_sparse_on_begin(10, threshold=3, test=False)
    t_save_sparse_on_begin(21, threshold=5, test=False)
    t_save_sparse_on_begin(19, threshold=10, test=False)

    # with capsys.disabled():
    #     t_save_sparse_on_begin(10, threshold=3, test=False)
    #     t_save_sparse_on_begin(21, threshold=5, test=False)
    #     t_save_sparse_on_begin(19, threshold=10, test=False)
