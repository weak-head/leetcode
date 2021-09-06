# flake8: noqa: F403, F405
import pytest
from leetcode.p1629_slowest_key import *

solutions = [
    slowestKey,
]

test_cases = [
    (
        [
            [9, 29, 49, 50],
            "cbcd",
        ],
        "c",
    ),
    (
        [
            [12, 23, 36, 46, 62],
            "spuda",
        ],
        "a",
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
