# flake8: noqa: F403, F405
import pytest
from leetcode.p0232_implement_queue_using_stacks import *

solutions = [
    MyQueue,
]

test_cases = [
    [
        ("empty", None, True),
        ("push", 1, None),
        ("empty", None, False),
        ("peek", None, 1),
        ("pop", None, 1),
        ("empty", None, True),
    ],
    [
        ("empty", None, True),
        ("push", 1, None),
        ("push", 2, None),
        ("push", 3, None),
        ("push", 4, None),
        ("empty", None, False),
        ("peek", None, 1),
        ("pop", None, 1),
        ("pop", None, 2),
        ("peek", None, 3),
        ("peek", None, 3),
        ("peek", None, 3),
        ("empty", None, False),
        ("pop", None, 3),
        ("peek", None, 4),
        ("pop", None, 4),
        ("empty", None, True),
    ],
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    q = solution()
    for m, arg, exp in args:
        if m == "push":
            q.push(arg)
        elif m == "peek":
            assert q.peek() == exp
        elif m == "pop":
            assert q.pop() == exp
        else:
            assert q.empty() == exp
