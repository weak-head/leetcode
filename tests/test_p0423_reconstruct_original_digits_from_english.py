# flake8: noqa: F403, F405
import pytest
from leetcode.p0423_reconstruct_original_digits_from_english import *

solutions = [
    originalDigits,
]

test_cases = [
    ("owoztneoer", "012"),
    ("fviefuro", "45"),
    ("zeroonetwothreefourfivesixseveneightnine", "0123456789"),
    ("zerozero", "00"),
    ("oonnee", "11"),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
