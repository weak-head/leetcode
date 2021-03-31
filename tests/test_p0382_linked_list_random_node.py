# flake8: noqa: F403, F405
import pytest
from leetcode.p0382_linked_list_random_node import *

solutions = [
    getRandom,
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("solution", solutions)
def test_solution(solution):
    a = [0, 1, 2, 3, 4, 5]
    h = [0, 0, 0, 0, 0, 0]
    l = to_list(a)
    n = 12_000
    for _ in range(n):
        ix = solution(l)
        h[ix] += 1

    # ~15% deviation is acceptable
    for v in h:
        assert 1_850 <= v <= 2_150


def to_list(a):
    c = dummy = ListNode(None)
    for v in a:
        c.next = ListNode(v)
        c = c.next
    return dummy.next
