import pytest
from leetcode.p0017_letter_combinations_of_a_phone_number import letterCombinations, letterCombinations2


@pytest.mark.parametrize(('number', 'combinations'), (
    ('23', ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
))
def test_letterCombinations(number, combinations):
    assert letterCombinations(number) == combinations