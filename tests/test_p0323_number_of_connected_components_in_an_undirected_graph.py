import pytest
from leetcode.p0323_number_of_connected_components_in_an_undirected_graph import (
    countComponents_bfs,
    countComponents_dfs,
    countComponents_sets,
)


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ((5, [[0, 1], [1, 2], [3, 4]]), (2)),
        ((5, [[0, 1], [1, 2], [2, 3], [3, 4]]), (1)),
    ),
)
def test_solve(a, expectation):
    assert countComponents_bfs(a[0], a[1]) == expectation
    assert countComponents_dfs(a[0], a[1]) == expectation
    assert countComponents_sets(a[0], a[1]) == expectation
