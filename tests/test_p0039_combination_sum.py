import pytest
from leetcode.p0039_combination_sum import combinationSum


@pytest.mark.parametrize(
    ("arr", "target", "expectation"),
    (([2, 3, 5], 8, [(2, 2, 2, 2), (2, 3, 3), (3, 5)]),),
)
def test_combination(arr, target, expectation):
    result = set(combinationSum(arr, target))
    assert len(result) == len(expectation)

    for e in expectation:
        assert e in result
