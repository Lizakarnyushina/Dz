import pytest
from dz_7.one import bfs


@pytest.mark.parametrize("graph, start, end, expected", [
    ({1: [2, 3], 2: [4], 3: [5], 4: [], 5: []}, 1, 5, 2),
    ({1: [2, 3], 2: [4], 3: [5], 4: [], 5: []}, 1, 4, 1),
    ({1: [2, 3], 2: [4], 3: [5], 4: [], 5: []}, 1, 6, None)
])
def test_bfs(graph, start, end, expected):
    assert bfs(graph, start, end) == expected