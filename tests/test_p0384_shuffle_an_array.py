# flake8: noqa: F403, F405
import pytest
from leetcode.p0384_shuffle_an_array import *

solutions = [
    Solution,
]


@pytest.mark.timeout(4)
@pytest.mark.parametrize("solution", solutions)
def test_solution(solution):

    # Monte Carlo method

    n = 100_000
    a = [1, 0, 0, 0, 0]
    cnt = [0, 0, 0, 0, 0]

    s = solution(a)

    for i in range(n):
        r = s.shuffle()

        for i in range(len(r)):
            if r[i] == 1:
                cnt[i] += 1
                break

    # we accept 20% deviation
    for freq in cnt:
        assert 18_000 <= freq <= 22_000
