# flake8: noqa: F403, F405
from functools import lru_cache
import pytest
from leetcode.p0460_lfu_cache import *

solutions = [
    LFUCache,
]

test_cases = [
    (
        [
            ["new", 2],
            ["p", 1, 1],
            ["p", 2, 2],
            ["g", 1],
            ["p", 3, 3],
            ["g", 2],
            ["g", 3],
            ["p", 4, 4],
            ["g", 1],
            ["g", 3],
            ["g", 4],
        ],
        [None, None, None, 1, None, -1, 3, None, -1, 3, 4],
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    capacity = args[0][1]
    c = solution(capacity)

    for i in range(1, len(args)):
        a = args[i][0]
        if a == "p":
            c.put(args[i][1], args[i][2])
        elif a == "g":
            assert c.get(args[i][1]) == expectation[i]
