import pytest
from collections import Counter
from one import f


@pytest.mark.parametrize(
    ('pl', 'k', 'end'),
    [
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([1, 2, 3, 4, 5], 3, [3, 4, 5, 1, 2]),
        ([1, 2], 3, [2, 1])
    ]
)
def test(pl, k, end):
    assert f(pl, k) == end