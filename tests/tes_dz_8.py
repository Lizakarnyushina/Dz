import pytest
from dz_8.one import *


@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([3, 2, 1, 5, 4], [1, 2, 3, 4, 5]),
        ([10, 5, 8, 3, 1, 9], [1, 3, 5, 8, 9, 10]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ],
)
def test_bubble_sort(input_list, expected):
    assert bubble_sort(input_list) == expected


@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([3, 2, 1, 5, 4], [1, 2, 3, 4, 5]),
        ([10, 5, 8, 3, 1, 9], [1, 3, 5, 8, 9, 10]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ],
)
def test_quick_sort(input_list, expected):
    assert quick_sort(input_list) == expected


@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([3, 2, 1, 5, 4], [1, 2, 3, 4, 5]),
        ([10, 5, 8, 3, 1, 9], [1, 3, 5, 8, 9, 10]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ],
)
def test_stalin_sort(input_list, expected):
    assert stalin_sort(input_list) == expected


@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([3, 2, 1, 5, 4], [1, 2, 3, 4, 5]),
        ([10, 5, 8, 3, 1, 9], [1, 3, 5, 8, 9, 10]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ],
)
def test_sleep_sort(input_list, expected):
    assert sleep_sort(input_list) == expected