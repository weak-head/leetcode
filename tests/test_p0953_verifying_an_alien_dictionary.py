import pytest
from leetcode.p0953_verifying_an_alien_dictionary import isAlienSorted


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ((["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"), (True)),
        ((["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"), (False)),
        ((["apple", "app"], "abcdefghijklmnopqrstuvwxyz"), (False)),
    ),
)
def test_solve(a, expectation):
    assert isAlienSorted(a[0], a[1]) == expectation
