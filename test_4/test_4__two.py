import pytest
from collections import Counter
from two import f


@pytest.mark.parametrize(
    ('n', 'end'),
    [
        (5, 120),
        (4, 24),
        (0, 1)
    ]
)
def test(n, end):
    assert f(n) == end