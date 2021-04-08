# flake8: noqa: F403, F405
import pytest
from leetcode.p0355_design_twitter import *

solutions = [
    Twitter,
]

test_cases = [
    [
        ("post", 1, 1),
        ("post", 1, 2),
        ("follow", 2, 1),
        ("unfollow", 2, 1),
        ("get", 1, [2, 1]),
        ("get", 2, []),
    ],
    [
        ("post", 1, 1),
        ("post", 1, 2),
        ("follow", 2, 1),
        ("unfollow", 2, 1),
        ("get", 1, [2, 1]),
        ("get", 2, []),
        ("follow", 2, 1),
        ("get", 2, [2, 1]),
        ("post", 1, 3),
        ("get", 2, [3, 2, 1]),
        ("unfollow", 2, 1),
        ("get", 2, []),
    ],
    [
        ("post", 1, 1),
        ("post", 2, 2),
        ("follow", 2, 1),
        ("follow", 1, 2),
        ("get", 1, [2, 1]),
        ("get", 2, [2, 1]),
        ("unfollow", 2, 1),
        ("unfollow", 1, 2),
        ("get", 2, [2]),
        ("get", 1, [1]),
    ],
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    t = solution()
    for method, a1, a2 in args:
        if method == "post":
            t.postTweet(a1, a2)
        elif method == "follow":
            t.follow(a1, a2)
        elif method == "unfollow":
            t.unfollow(a1, a2)
        elif method == "get":
            assert t.getNewsFeed(a1) == a2
