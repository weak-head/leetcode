# flake8: noqa: F403, F405
import pytest
from leetcode.p0284_peeking_iterator import *

solutions = [
    PeekingIterator,
]

#   ([args], expectation),
test_cases = [
    ([0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    it = solution(Iterator(args))

    i = 0
    while it.hasNext():
        assert it.peek() == expectation[i]
        assert it.next() == expectation[i]
        i += 1
