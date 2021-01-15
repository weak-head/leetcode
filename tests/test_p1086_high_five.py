import pytest
from leetcode.p1086_high_five import highFive


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            (
                [
                    [1, 91],
                    [1, 92],
                    [2, 93],
                    [2, 97],
                    [1, 60],
                    [2, 77],
                    [1, 65],
                    [1, 87],
                    [1, 100],
                    [2, 100],
                    [2, 76],
                ]
            ),
            ([(1, 87), (2, 88)]),
        ),
    ),
)
def test_highFive(a, expectation):
    assert highFive(a) == expectation
