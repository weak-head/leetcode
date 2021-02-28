# flake8: noqa: F403, F405
import pytest
from leetcode.p0895_maximum_frequency_stack import *

solutions = [
    FreqStack,
]

test_cases = [
    [
        ("push", 5, None),
        ("push", 7, None),
        ("push", 5, None),
        ("push", 7, None),
        ("push", 4, None),
        ("push", 5, None),
        ("pop", None, 5),
        ("pop", None, 7),
        ("pop", None, 5),
        ("pop", None, 4),
        ("pop", None, 7),
        ("pop", None, 5),
    ],
    [
        ("push", 1, None),
        ("pop", None, 1),
        ("push", 5, None),
        ("push", 3, None),
        ("push", 5, None),
        ("push", 5, None),
        ("push", 3, None),
        ("push", 1, None),
        ("push", 7, None),
        ("push", 9, None),
        ("pop", None, 5),
        ("pop", None, 3),
        ("pop", None, 5),
        ("pop", None, 9),
    ],
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    fs = solution()
    for method, arg, exp in args:
        if method == "push":
            fs.push(arg)
        else:
            assert fs.pop() == exp
