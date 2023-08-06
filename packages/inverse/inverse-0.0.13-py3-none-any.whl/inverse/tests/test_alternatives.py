from inverse.src.benchmarks.alternatives import main_alternatives
from inverse.tests.tdisplay import tdisplay


def test_main_alternatives(capsys):
    with capsys.disabled():
        tdisplay("main_alternatives")
        main_alternatives()
        assert True
