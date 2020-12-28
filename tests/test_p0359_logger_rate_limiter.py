import pytest
from leetcode.p0359_logger_rate_limiter import Logger


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            [[1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]],
            [True, True, False, False, False, True],
        ),
        (
            [
                [1, "foo"],
                [20, "bar"],
                [30, "foo"],
                [80, "bar"],
                [100, "foo"],
                [120, "foo"],
            ],
            [True, True, True, True, True, True],
        ),
    ),
)
def test_logger(a, expectation):
    logger = Logger()
    for ix, val in enumerate(a):
        assert logger.shouldPrintMessage(val[0], val[1]) == expectation[ix]
