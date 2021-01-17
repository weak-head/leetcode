import pytest
from leetcode.p1641_count_sorted_vowel_strings import countVowelStrings


@pytest.mark.parametrize(("a", "expectation"), (((1), (5)), ((2), (15)), (33, 66045)))
def test_solve(a, expectation):
    assert countVowelStrings(a) == expectation
