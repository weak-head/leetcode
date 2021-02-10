# flake8: noqa: F403, F405
import pytest
from leetcode.p0138_copy_list_with_random_pointer import *

solutions = [
    copyRandomList_hash,
    copyRandomList_pointers,
]

#   ([args], expectation),
test_cases = [
    (
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
    ),
    ([[1, 1], [2, 1]], [[1, 1], [2, 1]]),
    ([[3, None], [3, 0], [3, None]], [[3, None], [3, 0], [3, None]]),
    ([], []),
    ([[1, None]], [[1, None]]),
    ([[1, 0]], [[1, 0]]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    l = to_list(args)
    assert to_array(solution(l)) == expectation
    assert to_array(l) == args


def to_list(a):
    def to_l(a, ix, visited):
        if ix >= len(a):
            return None

        if ix in visited:
            return visited[ix]

        node = Node(a[ix][0])  # val
        visited[ix] = node

        node.next = to_l(a, ix + 1, visited)
        if a[ix][1] is not None:
            node.random = to_l(a, a[ix][1], visited)

        return node

    return to_l(a, 0, {})


def to_array(l):
    ix = 0
    cur = l
    while cur:
        cur.ix = ix
        cur = cur.next
        ix += 1

    a = []
    cur = l
    while cur:
        r = cur.random.ix if cur.random else None
        a.append([cur.val, r])
        cur = cur.next

    return a
