# flake8: noqa: F403, F405
import pytest
from leetcode.p0146_lru_cache import *

solutions = [
    LRUCache,
    LRUCache2,
]

test_cases = [
    [
        ("n", 4, None),
        ("g", 4, -1),
        ("p", 1, 1),
        ("p", 2, 2),
        ("p", 3, 3),
        ("p", 4, 4),
        ("p", 5, 5),
        ("g", 3, 3),
        ("g", 1, -1),
        ("p", 6, 6),
        ("g", 2, -1),
        ("g", 6, 6),
        ("p", 5, 5),
        ("p", 7, 7),
        ("g", 4, -1),
        ("g", 7, 7),
        ("g", 5, 5),
        ("g", 6, 6),
        ("g", 3, 3),
        ("p", 8, 8),
        ("g", 7, -1),
        ("g", 5, 5),
        ("p", 9, 9),
        ("g", 6, -1),
        ("g", 9, 9),
        ("g", 3, 3),
        ("g", 8, 8),
        ("g", 5, 5),
        ("g", 9, 9),
    ],
    [
        ("n", 1, None),
        ("g", 1, -1),
        ("p", 1, 1),
        ("g", 1, 1),
        ("p", 2, 2),
        ("g", 1, -1),
        ("g", 2, 2),
        ("g", 3, -1),
    ],
    [
        ("n", 2, None),
        ("p", 1, 1),
        ("p", 2, 2),
        ("p", 3, 3),
        ("g", 1, -1),
        ("p", 4, 4),
        ("g", 2, -1),
        ("g", 3, 3),
        ("p", 5, 5),
        ("g", 4, -1),
        ("g", 3, 3),
    ],
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    _, n, _ = args[0]
    lru = solution(n)

    for action, a1, a2 in args[1:]:
        if action == "g":
            assert lru.get(a1) == a2
        elif action == "p":
            lru.put(a1, a2)
