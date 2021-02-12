# flake8: noqa: F403, F405
import pytest
from leetcode.p0380_insert_delete_getrandom_o1 import *

solutions = [
    RandomizedSet,
]

#   ([args], expectation),
test_cases = [
    [
        ("d", 2, False),
        ("i", 1, True),
        ("i", 1, False),
        ("r", None, {1}),
    ],
    [
        ("d", 2, False),
        ("i", 1, True),
        ("i", 1, False),
        ("r", None, {1}),
        ("i", 2, True),
        ("i", 3, True),
        ("r", None, {1, 2, 3}),
        ("r", None, {1, 2, 3}),
        ("r", None, {1, 2, 3}),
        ("r", None, {1, 2, 3}),
        ("r", None, {1, 2, 3}),
    ],
    [
        ("d", 1, False),
        ("i", 1, True),
        ("r", None, {1}),
        ("r", None, {1}),
        ("r", None, {1}),
        ("i", 2, True),
        ("r", None, {1, 2}),
        ("r", None, {1, 2}),
        ("r", None, {1, 2}),
        ("r", None, {1, 2}),
        ("r", None, {1, 2}),
        ("d", 1, True),
        ("d", 1, False),
        ("r", None, {2}),
        ("r", None, {2}),
        ("r", None, {2}),
        ("d", 2, True),
        ("i", 3, True),
        ("r", None, {3}),
        ("r", None, {3}),
        ("r", None, {3}),
        ("r", None, {3}),
    ],
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    rs = solution()
    for m, v, e in args:
        if m == "i":
            assert rs.insert(v) == e
        elif m == "d":
            assert rs.remove(v) == e
        else:
            assert rs.getRandom() in e
