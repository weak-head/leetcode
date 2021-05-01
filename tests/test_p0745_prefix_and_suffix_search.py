# flake8: noqa: F403, F405
import pytest
from leetcode.p0745_prefix_and_suffix_search import *

solutions = [
    WordFilterTrieSetIntersect,
    WordFilterWrapped,
]

test_cases = [
    (
        ["apple"],
        ("a", "e", 0),
        ("app", "pple", 0),
        ("bb", "pple", -1),
    ),
    (
        ["apple", "bee", "anakee", "abeekeb"],
        ("a", "e", 2),
        ("app", "pple", 0),
        ("b", "e", 1),
        ("bee", "bee", 1),
        ("beef", "bee", -1),
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    w = solution(args[0])
    for pref, suf, ix in args[1:]:
        assert w.f(pref, suf) == ix
