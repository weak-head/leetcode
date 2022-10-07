# flake8: noqa: F403, F405
import pytest
from leetcode.p0295_find_median_from_data_stream import *

solutions = [
    MedianFinder,
]

test_cases = [
    (
        [
            ("add", 1),
            ("add", 2),
            ("find", None),
            ("add", 3),
            ("find", None),
        ],
        [None, None, 1.5, None, 2.0],
    ),
    (
        [
            ("add", 1),
            ("find", None),
        ],
        [None, 1],
    ),
    (
        [
            ("add", 1),
            ("add", 1),
            ("add", 1),
            ("add", 1),
            ("find", None),
            ("add", 1),
            ("find", None),
        ],
        [None, None, None, None, 1.0, None, 1.0],
    ),
    (
        [
            ("add", 5),
            ("add", 1),
            ("add", 1),
            ("add", 5),
            ("find", None),
            ("add", 10),
            ("find", None),
            ("add", 10),
            ("add", 10),
            ("find", None),
        ],
        [None, None, None, None, 3.0, None, 5.0, None, None, 5.0],
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    f = solution()
    for i in range(len(args)):
        if args[i][0] == "add":
            f.addNum(args[i][1])
        else:
            assert f.findMedian() == expectation[i]
