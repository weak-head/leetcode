# flake8: noqa: F403, F405
import pytest
from leetcode.p0706_design_hashmap import *

solutions = [
    MyHashMap,
]

test_cases = [
    [
        ("put", 1, 1),
        ("put", 2, 1),
        ("get", 2, 1),
        ("put", 2, 2),
        ("get", 2, 2),
        ("get", 3, -1),
        ("remove", 2, None),
        ("get", 2, -1),
    ],
    [
        ("put", 1, 1),
        ("put", 1, 2),
        ("get", 2, -1),
        ("put", 2, 1),
        ("get", 2, 1),
        ("get", 1, 2),
        ("remove", 1, None),
        ("remove", 2, None),
        ("get", 1, -1),
        ("get", 2, -1),
    ],
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    hm = solution()
    for m, a1, a2 in args:
        if m == "put":
            hm.put(a1, a2)
        elif m == "get":
            assert hm.get(a1) == a2
        elif m == "remove":
            hm.remove(a1)
