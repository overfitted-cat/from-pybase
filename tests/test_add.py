import pytest

from example.add import add_numbers


@pytest.mark.parametrize('a,b,res', [
    (0, 0, 0),
    (0, -1, -1),
    (-1, 0, -1),
    (-1, 1, 0),
])
def test_add_op(a, b, res):
    assert add_numbers(a, b) == res
