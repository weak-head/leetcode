# flake8: noqa: F403, F405
import enum
import pytest
from leetcode.p0398_random_pick_index import *

solutions = [
    Solution,
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("solution", solutions)
def test_solution(solution):
    a = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
    h = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    n = 12_000
    s = solution(a)

    for _ in range(n):
        ix = s.pick(1)
        h[ix] += 1

    for i, v in enumerate(h):
        if a[i]:
            assert 1_800 <= v <= 2_200
