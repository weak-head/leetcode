# flake8: noqa: F403, F405
import pytest
from leetcode.p0091_decode_ways import *

solutions = [
    num_decoding_dp,
    num_decoding_dp_bu,
    num_decodings_dp_td,
]

test_cases = [
    ("11106", 2),
    ("12", 2),
    ("1212", 5),
    ("12121212", 34),
    ("11111111", 34),
    ("111111111111", 233),
    ("1111111111111111", 1597),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
