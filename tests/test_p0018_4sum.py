import pytest
from leetcode.p0018_4sum import fourSum


@pytest.mark.parametrize(
    ("nums", "target", "expectation"),
    (
        ([], 0, []),
        ([1, 0, -1, 0, -2, 2], 0, [(-1, 0, 0, 1), (-2, -1, 1, 2), (-2, 0, 0, 2)]),
        ([1, 2, 3, 4, 5, 6, 7], 10, [(1, 2, 3, 4)]),
        ([1, 2, 3, 4, 5, 6, 7], 22, [(4, 5, 6, 7)]),
        (
            [1, 2, 3, 4, 5, 6, 7],
            18,
            [(3, 4, 5, 6), (1, 4, 6, 7), (2, 3, 6, 7), (2, 4, 5, 7)],
        ),
    ),
)
def test_fourSum(nums, target, expectation):
    res = fourSum(nums, target)

    res = sorted([tuple(sorted(k)) for k in res])
    exp = sorted([tuple(sorted(k)) for k in expectation])
    assert res == exp
