import pytest
from leetcode.p0017_letter_combinations_of_a_phone_number import (
    letterCombinations,
)


@pytest.mark.parametrize(
    ("number", "combinations"),
    (
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("45", ["gj", "gk", "gl", "hj", "hk", "hl", "ij", "ik", "il"]),
        ("", []),
    ),
)
def test_letterCombinations(number, combinations):
    assert sorted(letterCombinations(number)) == sorted(combinations)
