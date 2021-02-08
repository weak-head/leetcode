# flake8: noqa: F403, F405
import pytest
from leetcode.p1242_web_crawler_multithreaded import *

solutions = [
    crawl,
]


#   ([args], expectation),
test_cases = [
    (
        [
            "http://dom.com",
            {
                "http://dom.com": [
                    "http://dom.com",
                    "http://yam.com",
                    "http://pam.com",
                    "http://pom.com",
                    "http://dom.com/me",
                ],
                "http://dom.com/me": [
                    "http://dom.com/you",
                    "http://som.com",
                    "http://jom.com",
                ],
                "http://dom.com/you": ["http://dom.com/me"],
            },
        ],
        {"http://dom.com", "http://dom.com/me", "http://dom.com/you"},
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    root = args[0]
    h = HtmlParser(args[1])
    assert solution(root, h) == expectation
