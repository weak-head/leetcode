# flake8: noqa: F403, F405
import pytest
from leetcode.p0990_satisfiability_of_equality_equations import *

solutions = [
    equationsPossible,
]

test_cases = [
    (["a==b", "b!=a"], False),
    (["b==a", "a==b"], True),
    (["a==b", "b==c", "a==c"], True),
    (["a==b", "b!=c", "c==a"], False),
    (["c==c", "b==d", "x!=z"], True),
    (["c==c", "b==d", "x!=z", "z!=b", "b!=c", "c!=z"], True),
    (
        [
            "c==c",
            "b==d",
            "x!=z",
            "z!=b",
            "b!=c",
            "c!=z",
            "z!=k",
            "k!=f",
            "f==c",
            "x==f",
            "j==x",
            "x!=b",
            "j==k",
        ],
        False,
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
