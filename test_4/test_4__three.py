import pytest
from collections import Counter
from three import f


@pytest.mark.parametrize(
    'pos',
    [
        [34, 'Hello, world!', False],
        '12345',
        tuple([23, '23']),
        [1, True],
    ]
)
def test_true(pos):
    assert f(pos) is True


@pytest.mark.parametrize(
    'pos',
    [
        '1113',
        tuple([7, 7]),
    ]
)
def test_false(pos):
    assert f(pos) is False