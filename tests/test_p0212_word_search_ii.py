# flake8: noqa: F403, F405
import pytest
from leetcode.p0212_word_search_ii import *

solutions = [
    findWords,
    findWords_optimized,
]

test_cases = [
    (
        [
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
        ],
        ["eat", "oath"],
    ),
    (
        [[["a", "b"], ["c", "d"]], ["abcb"]],
        [],
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert set(solution(*args)) == set(expectation)
