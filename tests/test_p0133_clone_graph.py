# flake8: noqa: F403, F405
import pytest
from leetcode.p0133_clone_graph import *

solutions = [
    cloneGraph,
]

#   ([args], expectation),
test_cases = [
    (
        [3, [[1], [0, 1, 2], [1]]],
        [3, [[1], [0, 1, 2], [1]]],
    ),
    (
        [5, [[1], [2], [3], [4], [0]]],
        [5, [[1], [2], [3], [4], [0]]],
    ),
    (
        [5, [[1, 2, 3], [3, 1, 4], [2, 4], [0, 1], [0]]],
        [5, [[1, 2, 3], [3, 1, 4], [2, 4], [0, 1], [0]]],
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert compare(solution(get_graph(*args)), get_graph(*expectation))


def get_graph(n, cons):
    nodes = [Node(i) for i in range(n)]

    for ix, connections in enumerate(cons):
        for con in connections:
            nodes[ix].neighbors.append(nodes[con])

    return nodes[0]


def compare(a, b, compared={}):
    if a is None and b is None:
        return True

    if a is None or b is None:
        return False

    if a in compared:
        return compared[a]

    if a.val != b.val:
        return False

    if len(a.neighbors) != len(b.neighbors):
        return False

    compared[a] = True
    for ac, bc in zip(a.neighbors, b.neighbors):
        if not compare(ac, bc, compared):
            return False

    return True
