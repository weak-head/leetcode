import pytest
from leetcode.p0002_add_two_numbers import Solution, from_array, to_array


@pytest.mark.parametrize(
    ("first", "second", "expectation"),
    (
        (None, None, None),
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([2, 4, 3, 1, 2, 7], [5, 6, 4, 0, 0, 4], [7, 0, 8, 1, 2, 1, 1]),
        ([2, 4, 3], [5, 6, 4, 0, 0, 4], [7, 0, 8, 0, 0, 4]),
        ([5, 6, 4, 0, 0, 4], None, [5, 6, 4, 0, 0, 4]),
        (None, [5, 6, 4, 0, 0, 4], [5, 6, 4, 0, 0, 4]),
    ),
)
def test_addTwoNumbers(first, second, expectation):
    s = Solution()

    l1 = from_array(first) if first else None
    l2 = from_array(second) if second else None

    res = s.addTwoNumbers(l1, l2)
    res = to_array(res) if res else None

    assert res == expectation
