# flake8: noqa: F403, F405
import pytest
from leetcode.p0936_stamping_the_sequence import *

solutions = [
    movesToStamp,
]

test_cases = [
    (["abca", "aabcaca"]),
    (["abc", "ababc"]),
    (["abc", "aaaaabc"]),
    (["abc", "abcccccc"]),
    (["abc", "aaabcabccccc"]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    stamp, target = args
    sequence = solution(stamp, target)
    assert apply(stamp, len(target), sequence) == target


def apply(stamp, n, indexes):
    target = ["?"] * n
    for i in indexes:
        for j in range(len(stamp)):
            target[i + j] = stamp[j]
    return "".join(target)
