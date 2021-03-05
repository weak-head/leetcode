# flake8: noqa: F403, F405
import pytest
from leetcode.p0078_subsets import *

solutions = [
    subsets_induction,
    subsets_backtracking,
]

test_cases = [
    ([], [[]]),
    ([1], [[1], []]),
    ([1, 2], [[2, 1], [2], [1], []]),
    ([1, 2, 3], [[3, 2, 1], [3, 2], [3, 1], [3], [2, 1], [2], [1], []]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    res = solution(list(args))
    rs = set(map(tuple, map(sorted, res)))
    es = set(map(tuple, map(sorted, expectation)))
    assert rs == es
