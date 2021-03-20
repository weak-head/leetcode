# flake8: noqa: F403, F405
import pytest
from leetcode.p1396_design_underground_system import *

solutions = [
    UndergroundSystem,
]

test_cases = [
    [
        ("in", 1, "a", 0),
        ("out", 1, "b", 3),
        ("avg", "a", "b", 3),
    ],
    [
        ("in", 1, "a", 0),
        ("in", 2, "b", 0),
        ("out", 1, "b", 3),
        ("out", 2, "a", 4),
        ("avg", "a", "b", 3),
        ("avg", "b", "a", 4),
    ],
    [
        ("in", 1, "a", 0),
        ("out", 1, "b", 3),
        ("in", 2, "a", 5),
        ("out", 2, "b", 15),
        ("in", 1, "a", 20),
        ("out", 1, "b", 40),
        ("avg", "a", "b", 11),
    ],
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    s = solution()
    for action, a, b, c in args:
        if action == "in":
            s.checkIn(a, b, c)
        elif action == "out":
            s.checkOut(a, b, c)
        elif action == "avg":
            assert s.getAverageTime(a, b) == c
