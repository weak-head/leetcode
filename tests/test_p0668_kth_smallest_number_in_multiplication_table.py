import pytest
from leetcode.p0668_kth_smallest_number_in_multiplication_table import (
    find_kth_1,
    find_kth_2,
    find_kth_3,
)


@pytest.mark.parametrize(("n", "m", "k", "r"), ((3, 3, 5, 3), (2, 3, 6, 6)))
def test_find(n, m, k, r):
    assert find_kth_1(n, m, k) == r
    assert find_kth_2(n, m, k) == r
    assert find_kth_3(n, m, k) == r
