import pytest
from leetcode.p0029_divide_two_integers import divide


@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    ("dividend", "divisor", "result"),
    (
        (1, 1, 1),
        (10, 3, 3),
        (10, -3, -3),
        (-10, 3, -3),
        (-10, -3, 3),
        (1234321, 1, 1234321),
        (-(2 ** 31), -1, 2 ** 31 - 1),
        (2 ** 31 - 1, -1, (-(2 ** 31)) + 1),
        (2 ** 10, 2, 2 ** 9),
        (2 ** 20, 2 ** 10, 2 ** 10),
    ),
)
def test_divide(dividend, divisor, result):
    assert divide(dividend, divisor) == result
