# flake8: noqa: F403, F405
import pytest
from leetcode.p0622_design_circular_queue import *

solutions = [
    MyCircularQueue,
]

test_cases = [
    [
        ("new", 3, None),
        ("front", None, -1),
        ("rear", None, -1),
        ("isempty", None, True),
        ("isfull", None, False),
        ("dequeue", None, False),
        ("enqueue", 1, True),
        ("isempty", None, False),
        ("enqueue", 2, True),
        ("enqueue", 3, True),
        ("enqueue", 4, False),
        ("front", None, 1),
        ("rear", None, 3),
        ("isempty", None, False),
        ("isfull", None, True),
        ("dequeue", None, True),
        ("isfull", None, False),
        ("isempty", None, False),
        ("front", None, 2),
        ("rear", None, 3),
        ("enqueue", 4, True),
        ("front", None, 2),
        ("rear", None, 4),
        ("isfull", None, True),
        ("dequeue", None, True),
        ("isfull", None, False),
        ("dequeue", None, True),
        ("dequeue", None, True),
        ("dequeue", None, False),
        ("isfull", None, False),
        ("isempty", None, True),
    ],
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    q = solution(args[0][1])
    for m, arg, res in args[1:]:
        if m == "front":
            assert q.Front() == res
        elif m == "rear":
            assert q.Rear() == res
        elif m == "isempty":
            assert q.isEmpty() == res
        elif m == "isfull":
            assert q.isFull() == res
        elif m == "dequeue":
            assert q.deQueue() == res
        elif m == "enqueue":
            assert q.enQueue(arg) == res
