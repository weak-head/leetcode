# flake8: noqa: F403, F405
import pytest
from leetcode.p0609_find_duplicate_file_in_system import *

solutions = [
    findDuplicate,
]

test_cases = [
    (
        [
            "root/a 1.txt(abcd) 2.txt(efgh)",
            "root/c 3.txt(abcd)",
            "root/c/d 4.txt(efgh)",
            "root 4.txt(efgh)",
        ],
        [
            ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"],
            ["root/a/1.txt", "root/c/3.txt"],
        ],
    ),
    (
        [
            "root/a 1.txt(abcd) 2.txt(efgh)",
            "root/c 3.txt(abcd)",
            "root/c/d 4.txt(efgh)",
        ],
        [["root/a/2.txt", "root/c/d/4.txt"], ["root/a/1.txt", "root/c/3.txt"]],
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    res = solution(args)
    res_exp = [set(val) for val in expectation]
    assert len(res) == len(res_exp)
    for r in res:
        assert r in res_exp
    for r in res_exp:
        assert r in res
