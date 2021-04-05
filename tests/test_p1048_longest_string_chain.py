# flake8: noqa: F403, F405
import pytest
from leetcode.p1048_longest_string_chain import *

solutions = [
    longestStrChain_group,
    longestStrChain_sort,
]

test_cases = [
    (["a", "b", "ba", "bca", "bda", "bdca"], 4),
    (["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], 5),
    (["abc", "def"], 1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
