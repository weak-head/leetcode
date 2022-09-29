# flake8: noqa: F403, F405
import pytest
from leetcode.p0787_cheapest_flights_within_k_stops import *

solutions = [
    findCheapestPrice1,
    findCheapestPrice2,
]

test_cases = [
    (
        [4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1],
        700,
    ),
    ([3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1], 200),
    ([3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0], 500),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
