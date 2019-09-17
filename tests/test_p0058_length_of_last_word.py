import pytest
from leetcode.p0058_length_of_last_word import length_of_last_word


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ("", 0),
        (" ", 0),
        ("   ", 0),
        ("a", 1),
        (" a", 1),
        ("a ", 1),
        (" abc ", 3),
        ("  abc  ", 3),
        ("  abc aabc  ", 4),
        ("abcaabc  ", 7),
        ("  abcaabc", 7),
    ),
)
def test_len(a, expectation):
    assert length_of_last_word(a) == expectation
