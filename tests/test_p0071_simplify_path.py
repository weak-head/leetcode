import pytest
from leetcode.p0071_simplify_path import simplifyPath


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (("/a/./b/../../c/"), ("/c")),
        (("/../"), ("/")),
        (("/../../../../../"), ("/")),
        (("/../../../../../c/../b/"), ("/b")),
        (("/../../../../../c/./////b/"), ("/c/b")),
    ),
)
def test_solve(a, expectation):
    assert simplifyPath(a) == expectation
