# flake8: noqa: F403, F405
import pytest
from leetcode.p0354_russian_doll_envelopes import *

solutions = [
    maxEnvelopes,
]

test_cases = [
    ([[5, 4], [6, 4], [6, 7], [2, 3]], 3),
    ([[1, 1], [1, 1], [1, 1]], 1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
