from src import script


def test_add1():
    assert script.add1(1) == 2
    assert script.add1(1.1) == 2.1
