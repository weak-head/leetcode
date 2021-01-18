import pytest
from leetcode.p0459_repeated_substring_pattern import repeatedSubstringPattern


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (("abc"), (False)),
        (("abcabc"), (True)),
        (("ababab"), (True)),
        (("abcbab"), (False)),
        (("bccb"), (False)),
    ),
)
def test_solve(a, expectation):
    assert repeatedSubstringPattern(a) == expectation
