# flake8: noqa: F403, F405
import pytest
from leetcode.p0535_encode_and_decode_tinyurl import *

solutions = [
    Codec,
]

test_cases = [
    ("abc"),
    ("1abc"),
    ("abc4"),
    ("4abc4"),
    ("4a/com/bc4"),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    url = f"http://tinyurl.com/{args}"
    codec = solution()
    tiny = codec.encode(url)
    assert codec.decode(tiny) == url
