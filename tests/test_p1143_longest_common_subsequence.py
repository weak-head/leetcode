# flake8: noqa: F403, F405
import pytest
from leetcode.p1143_longest_common_subsequence import *

solutions = [
    lcs_bu_optimized,
    lcs_bu,
    lcs_td,
]

test_cases = [
    (["", "d"], 0),
    (["d", ""], 0),
    (["abcbd", "bb"], 2),
    (["123321", "abc"], 0),
    (["123321", "2sdf3bb2ab1"], 4),
    (["abcdeddfsjesjaeh4nflshe;sheajs", "fhslenbhshdkloenshfpbhendfh"], 10),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
