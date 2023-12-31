import pytest
from dz_5.one import binary_search


@pytest.mark.parametrize("x, y, esequencepected", [ 
    ([1, 2, 3, 4, 5], 3, 2), 
    ([1, 2, 3, 4, 5], 6, None), 
    ([1, 2, 2, 3, 4, 5], 2, 1), 
    ([], 42, None),
    ([0], 0, 0),
    ([0], 1, None),
    ([-1, 0, 42], 0, 1),
    ([-42, 0, 42], 42, 2),
    ([-6, -5, -4, -3, -2, -1], -4, 2),
    ([1, 2, 3, 4, 5, 6], 4, 3),
    ([1, 2, 3, 4, 5, 6, 7], 4, 3),
    ([1, 2, 3, 4, 5], 7, None),
    ([1, 2, 3, 4, 5, 6], 7, None),
    ([42, 42, 42, 42, 42], 42, 0),
    ([-42, -42, -42, -42, -42], -42, 0),
    ([42, 42, 42, 42, 43], 43, 4),
    ([41, 42, 42, 42, 42], 41, 0),
    ([-2, -2, -1, 0, 1, 2, 2, 2], -1, 2),
    ([-2, -2, -1, 0, 1, 1, 2, 2], 1, 4)
]) 
def test_binary_search(x, y, esequencepected): 
    assert binary_search(x, y) == esequencepected