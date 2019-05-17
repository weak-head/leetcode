import pytest
from leetcode.p0040_combination_sum_ii import combinationSum


@pytest.mark.parametrize(
    ("arr", "target", "expectation"),
    (
        ([10, 1, 2, 7, 6, 1, 5], 8, {(1, 7), (1, 2, 5), (2, 6), (1, 1, 6)}),
        ([2, 5, 2, 1, 2], 5, {(1, 2, 2), (5,)}),
    ),
)
def test_combination(arr, target, expectation):
    verify(arr, target, expectation, combinationSum)


def verify(arr, target, expectation, func):
    result = func(arr, target)
    assert len(result) == len(expectation)

    for r in result:
        assert tuple(sorted(r)) in expectation
