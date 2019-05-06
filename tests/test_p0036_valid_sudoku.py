import pytest
from leetcode.p0036_valid_sudoku import isValidSudoku


@pytest.mark.parametrize(('a', 'expectation'), (
    (None, False),
))
def test_sudoku(a, expectation):
    assert isValidSudoku(a) == expectation
