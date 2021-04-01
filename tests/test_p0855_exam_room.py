# flake8: noqa: F403, F405
import pytest
from leetcode.p0855_exam_room import *

solutions = [
    ExamRoom,
    ExamRoomPQ,
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
    [
        ("n", 100),
        ("s", 0),
        ("s", 99),
        ("s", 49),
        ("s", 74),
        ("s", 24),
        ("s", 12),
        ("l", 49),
        ("l", 74),
        ("s", 61),
        ("s", 80),
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
