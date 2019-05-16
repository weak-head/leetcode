import pytest
from leetcode.p0039_combination_sum import combinationSum, combinationSum2


@pytest.mark.parametrize(
    ("arr", "target", "expectation"),
    (([2, 3, 5], 8, [(2, 2, 2, 2), (2, 3, 3), (3, 5)]),),
)
def test_combination(arr, target, expectation):
    verify(arr, target, expectation, combinationSum)
    verify(arr, target, expectation, combinationSum2)


def verify(arr, target, expectation, func):
    result = set(func(arr, target))
    assert len(result) == len(expectation)

    for e in expectation:
        assert e in result
