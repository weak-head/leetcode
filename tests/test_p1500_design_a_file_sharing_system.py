# flake8: noqa: F403, F405
import pytest
from leetcode.p1500_design_a_file_sharing_system import *

solutions = [
    FileSharing,
]

test_cases = [
    [
        ("new", 17, None),
        ("join", [], 1),
        ("join", [6, 8, 7, 15, 16, 9, 10, 4, 13, 12, 5, 14, 1, 11, 2, 17, 3], 2),
        ("join", [9, 11, 14, 16, 10, 6, 1, 15, 12], 3),
        ("join", [], 4),
        ("join", [17, 10, 16], 5),
        ("req", [1, 6], [2, 3]),
        ("req", [1, 1], [2, 3]),
        ("req", [1, 13], [2]),
        ("req", [5, 15], [2, 3]),
        ("req", [3, 5], [2]),
        ("req", [3, 4], [2]),
        ("req", [1, 4], [2, 3]),
        ("req", [1, 7], [2]),
        ("req", [2, 15], [2, 3, 5]),
        ("leave", 5, None),
        ("req", [2, 15], [2, 3]),
    ]
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    fs = solution(args[0][1])
    for m, p, r in args[1:]:
        if m == "join":
            assert fs.join(p) == r
        elif m == "req":
            assert fs.request(p[0], p[1]) == r
        elif m == "leave":
            fs.leave(p)
