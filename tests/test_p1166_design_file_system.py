import pytest
from leetcode.p1166_design_file_system import FileSystem


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            (
                ["createPath", "createPath", "get", "createPath", "get"],
                [
                    ["/leet", 1],
                    ["/leet/code", 2],
                    ["/leet/code"],
                    ["/leet/code", 3],
                    ["/leet/code"],
                ],
            ),
            ([True, True, 2, False, 2]),
        ),
        (
            (
                ["createPath", "createPath", "createPath", "get", "get", "get", "get"],
                [
                    ["/a", 1],
                    ["/a/b", 2],
                    ["/a/b/c", 3],
                    ["/a"],
                    ["/a/b"],
                    ["/a/c"],
                    ["/c"],
                ],
            ),
            ([True, True, True, 1, 2, -1, -1]),
        ),
    ),
)
def test_solve(a, expectation):
    fs = FileSystem()
    for m, v, e in zip(a[0], a[1], expectation):
        if m == "createPath":
            assert fs.createPath(v[0], v[1]) == e
        elif m == "get":
            assert fs.get(v[0]) == e
