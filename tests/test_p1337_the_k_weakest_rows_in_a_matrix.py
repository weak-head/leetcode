# flake8: noqa: F403, F405
import pytest
from leetcode.p1337_the_k_weakest_rows_in_a_matrix import *

solutions = [
    kWeakestRows_heap_bs,
    kWeakestRows_vertical,
]

test_cases = [
    (
        [
            [
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1],
            ],
            3,
        ],
        [2, 0, 3],
    ),
    (
        [
            [
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
            ],
            3,
        ],
        [
            0,
            1,
            2,
        ],
    ),
    (
        [
            [
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
            ],
            4,
        ],
        [0, 1, 2, 3],
    ),
    (
        [
            [
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
            ],
            5,
        ],
        [0, 1, 2, 3, 4],
    ),
    (
        [
            [
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 0, 0, 0, 0],
            ],
            5,
        ],
        [4, 3, 2, 1, 0],
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert list(solution(*args)) == expectation
