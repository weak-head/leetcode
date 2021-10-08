# flake8: noqa: F403, F405
import pytest
from leetcode.p0208_implement_trie_prefix_tree import *

solutions = [
    Trie,
]

test_cases = [
    [
        ("i", "apple", None),
        ("s", "apple", True),
        ("sw", "app", True),
        ("s", "app", False),
        ("s", "bbb", False),
        ("sw", "a", True),
        ("sw", "b", False),
    ],
    [
        ("i", "app", None),
        ("i", "apps", None),
        ("i", "apple", None),
        ("s", "apps", True),
        ("s", "app", True),
        ("s", "ap", False),
        ("sw", "ap", True),
        ("sw", "appb", False),
        ("s", "apple", True),
    ],
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    t = solution()
    for action, word, result in args:
        if action == "i":
            t.insert(word)
        elif action == "s":
            assert t.search(word) == result
        elif action == "sw":
            assert t.startsWith(word) == result
