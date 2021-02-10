# flake8: noqa: F403, F405
import pytest
from leetcode.p0237_integer_to_english_words import *

solutions = [
    numberToWords,
]

#   ([args], expectation),
test_cases = [
    (0, "Zero"),
    (217, "Two Hundred Seventeen"),
    (123, "One Hundred Twenty Three"),
    (12345, "Twelve Thousand Three Hundred Forty Five"),
    (1234567, "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"),
    (
        1234567891,
        "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One",
    ),
    (
        719234567891,
        "Seven Hundred Nineteen Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One",
    ),
    (
        14719234567891,
        "Fourteen Trillion Seven Hundred Nineteen Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One",
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
