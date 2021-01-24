import pytest
from leetcode.p0727_minimum_window_subsequence import minWindow1, minWindow2


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (("fgrqsqsnodwmxzkzxwqegkndaa", "fnok"), ("fgrqsqsnodwmxzk")),
        (("abcdebdde", "bde"), ("bcde")),
    ),
)
def test_solve(a, expectation):
    assert minWindow1(a[0], a[1]) == expectation
    assert minWindow2(a[0], a[1]) == expectation
