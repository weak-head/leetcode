import pytest
from leetcode.p0039_combination_sum import (
    combinationSum,
    combinationSum2,
    combinationSum3,
)

test_cases = (
    ([2, 3, 5], 8, {(2, 2, 2, 2), (2, 3, 3), (3, 5)}),
    ([2, 3, 6, 7], 7, {(7,), (2, 2, 3)}),
)


@pytest.mark.parametrize(("arr", "target", "expectation"), test_cases)
def test_combination(arr, target, expectation):
    verify(arr, target, expectation, combinationSum)


@pytest.mark.parametrize(("arr", "target", "expectation"), test_cases)
def test_combination2(arr, target, expectation):
    verify(arr, target, expectation, combinationSum2)


@pytest.mark.parametrize(("arr", "target", "expectation"), test_cases)
def test_combination3(arr, target, expectation):
    verify(arr, target, expectation, combinationSum3)


def verify(arr, target, expectation, func):
    result = func(arr, target)
    assert len(result) == len(expectation)

    for r in result:
        assert tuple(sorted(r)) in expectation
