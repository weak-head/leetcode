# flake8: noqa: F403, F405
import pytest
from leetcode.p1041_robot_bounded_in_circle import *

solutions = [
    isRobotBounded,
]

#   ([args], expectation),
test_cases = [
    ("GGLLGG", True),
    ("GG", False),
    ("GL", True),
    ("GRGL", False),
    ("GGGLGLGRRGG", False),
    ("GRGL", False),
    ("GGGLGLGLGG", True),
    ("GGGLGLGLGGGGGGGGGGGGGGGGG", True),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
