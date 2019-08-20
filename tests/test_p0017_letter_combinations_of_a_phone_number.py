import pytest
from leetcode.p0017_letter_combinations_of_a_phone_number import (
    letterCombinations,
    letterCombinations2,
    letterCombinations3,
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
    assert letterCombinations(number) == combinations
    assert letterCombinations2(number) == combinations
    assert letterCombinations3(number) == combinations
