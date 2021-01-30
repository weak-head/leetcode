import pytest
from leetcode.p1675_minimize_deviation_in_array import minimumDeviation


@pytest.mark.parametrize(
    ("a", "expectation"), ((([1, 2, 1, 2, 1, 2, 1]), (0)), (([1, 2, 3, 4]), (1)))
)
def test_solve(a, expectation):
    assert minimumDeviation(a) == expectation
