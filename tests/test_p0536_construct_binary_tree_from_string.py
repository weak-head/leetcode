# flake8: noqa: F403, F405
import pytest
from leetcode.p0536_construct_binary_tree_from_string import *

solutions = [
    str2tree,
    str2tree_ix,
]

test_cases = [
    ("4(2(3)(1))(6(5))", [4, 2, 6, 3, 1, 5]),
    ("4(2(3)(1))(6(5)(7))", [4, 2, 6, 3, 1, 5, 7]),
    ("-4(2(3)(1))(6(5)(7))", [-4, 2, 6, 3, 1, 5, 7]),
    ("1(2(7))(3(4)(5)", [1, 2, 3, 7, 4, 5]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert array(solution(args)) == expectation


def array(node):
    a = []
    q = deque([node])
    while q:
        n = q.popleft()
        a.append(n.val)

        if n.left:
            q.append(n.left)

        if n.right:
            q.append(n.right)

    return a
