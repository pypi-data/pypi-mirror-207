def convert_scikit_bunch_to_pd_df(bunch):
    import pandas as pd
    return pd.DataFrame(bunch.data, columns=bunch.feature_names)


def test_convert(capsys):
    from sklearn.datasets import fetch_california_housing

    with capsys.disabled():
        data_bunch = fetch_california_housing()
        df = convert_scikit_bunch_to_pd_df(data_bunch)
        # print(df.shape )
        assert df.shape == (20640, 8)


if __name__ == "__main__":
    test_convert(None )
