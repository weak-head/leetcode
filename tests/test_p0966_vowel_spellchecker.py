# flake8: noqa: F403, F405
import pytest
from leetcode.p0966_vowel_spellchecker import *

solutions = [
    spellchecker,
]

test_cases = [
    (
        [
            ["KiTe", "kite", "hare", "Hare"],
            [
                "kite",
                "Kite",
                "KiTe",
                "Hare",
                "HARE",
                "Hear",
                "hear",
                "keti",
                "keet",
                "keto",
            ],
        ],
        ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"],
    )
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
