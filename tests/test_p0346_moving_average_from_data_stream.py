import pytest
from leetcode.p0346_moving_average_from_data_stream import MovingAverage


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ((3, [1, 10, 3, 5]), ([1.0, 5.5, float(14 / 3), 6.0])),
        ((1, [1, 10, 3, 5]), ([1.0, 10, 3, 5])),
        ((100, [1, 10, 3, 5]), ([1.0, 5.5, float(14 / 3), float(19 / 4)])),
    ),
)
def test_average(a, expectation):
    size, values = a
    m = MovingAverage(size)
    for v, e in zip(values, expectation):
        assert m.next(v) == e
