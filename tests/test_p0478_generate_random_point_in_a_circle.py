# flake8: noqa: F403, F405
import pytest
from leetcode.p0478_generate_random_point_in_a_circle import *

solutions = [
    Solution,
]

test_cases = [
    ([1.0, 0.0, 0.0, 100]),
    ([5.0, 1.0, 2.5, 100]),
    ([500.0, 111.5, -27.55, 100]),
    ([5000.0, 7111.5, -2727.55, 1000]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    r, x, y, samples = args
    s = solution(r, x, y)

    for _ in range(samples):
        xr, yr = s.randPoint()

        assert (xr - x) ** 2 + (yr - y) ** 2 <= r ** 2
