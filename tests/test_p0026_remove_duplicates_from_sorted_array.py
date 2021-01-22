import pytest
from leetcode.p0026_remove_duplicates_from_sorted_array import removeDuplicates


@pytest.mark.parametrize(
    ("list", "result"),
    (([0, 0, 0, 1, 1, 1, 2, 3, 3, 4, 4, 4, 5], [0, 1, 2, 3, 4, 5]), ([], [])),
)
def test_remove_duplicates(list, result):
    ix = removeDuplicates(list)
    assert ix == len(result)
    for i in range(0, ix):
        assert list[i] == result[i]
