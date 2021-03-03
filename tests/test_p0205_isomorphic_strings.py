# flake8: noqa: F403, F405
import pytest
from leetcode.p0205_isomorphic_strings import *

solutions = [
    isIsomorphic,
]

test_cases = [
    (["egg", "add"], True),
    (["foo", "bar"], False),
    (["paper", "title"], True),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation


follow_up_solutions = [
    group_isomorphic,
]

follow_up_test_cases = [
    (
        ["aab", "xxy", "xyz", "abc", "def", "xyx"],
        [["aab", "xxy"], ["xyz", "abc", "def"], ["xyx"]],
    ),
    (
        ["bc", "dd", "cc", "cb", "aa", "ax", "foo", "bar", "kff", "ddd"],
        [
            ["bc", "cb", "ax"],
            ["dd", "cc", "aa"],
            ["foo", "kff"],
            ["bar"],
            ["ddd"],
        ],
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), follow_up_test_cases)
@pytest.mark.parametrize("solution", follow_up_solutions)
def test_follow_up_solution(args, expectation, solution):
    assert solution(args) == expectation
