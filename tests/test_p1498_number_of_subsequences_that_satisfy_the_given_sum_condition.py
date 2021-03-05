# flake8: noqa: F403, F405
import pytest
from leetcode.p1498_number_of_subsequences_that_satisfy_the_given_sum_condition import *

solutions = [
    numSubseq,
]

test_cases = [
    ([[3, 5, 6, 7], 9], 4),
    (
        [
            [
                14,
                4,
                6,
                6,
                20,
                8,
                5,
                6,
                8,
                12,
                6,
                10,
                14,
                9,
                17,
                16,
                9,
                7,
                14,
                11,
                14,
                15,
                13,
                11,
                10,
                18,
                13,
                17,
                17,
                14,
                17,
                7,
                9,
                5,
                10,
                13,
                8,
                5,
                18,
                20,
                7,
                5,
                5,
                15,
                19,
                14,
            ],
            22,
        ],
        272187084,
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
