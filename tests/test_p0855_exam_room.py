# flake8: noqa: F403, F405
import pytest
from leetcode.p0855_exam_room import *

solutions = [
    ExamRoom,
]

test_cases = [
    [
        ("n", 10),
        ("s", 0),
        ("s", 9),
        ("s", 4),
        ("s", 2),
        ("l", 4),
        ("s", 5),
    ],
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    s = solution(args[0][1])
    for m, v in args[1:]:
        if m == "s":
            assert s.seat() == v
        elif m == "l":
            s.leave(v)
