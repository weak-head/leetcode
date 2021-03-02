# flake8: noqa: F403, F405
import pytest
from leetcode.p0225_implement_stack_using_queues import *

solutions = [
    MyStack,
]

test_cases = [
    [
        ("empty", True),
        ("push", 1),
        ("top", 1),
        ("empty", False),
        ("pop", 1),
        ("empty", True),
    ],
    [
        ("empty", True),
        ("push", 1),
        ("push", 2),
        ("push", 3),
        ("push", 4),
        ("top", 4),
        ("empty", False),
        ("pop", 4),
        ("top", 3),
        ("pop", 3),
        ("top", 2),
        ("empty", False),
        ("pop", 2),
        ("pop", 1),
        ("empty", True),
    ],
    [
        ("push", 1),
        ("push", 2),
        ("push", 3),
        ("pop", 3),
        ("push", 5),
        ("pop", 5),
        ("push", 10),
        ("push", 11),
        ("pop", 11),
        ("pop", 10),
        ("push", 7),
        ("pop", 7),
        ("pop", 2),
        ("pop", 1),
    ],
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    s = solution()
    for m, arg in args:
        if m == "push":
            s.push(arg)
        elif m == "empty":
            assert s.empty() == arg
        elif m == "pop":
            assert s.pop() == arg
        elif m == "top":
            assert s.top() == arg
        else:
            assert False
