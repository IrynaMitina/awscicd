import pytest
import fibo_lib


def test_fibonacci_num():
    assert 1 == fibo_lib.fibonacci_num(0)
    assert 1 == fibo_lib.fibonacci_num(1)
    assert 2 == fibo_lib.fibonacci_num(2)
    assert 3 == fibo_lib.fibonacci_num(3)
    assert 5 == fibo_lib.fibonacci_num(4)


@pytest.mark.skip
def test_failed():
    assert 3 == fibo_lib.fibonacci_num(0)
