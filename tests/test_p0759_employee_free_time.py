import pytest
from leetcode.p0759_employee_free_time import (
    Interval,
    employeeFreeTime1,
    employeeFreeTime2,
)


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]), ([(3, 4)])),
        (([[[1, 2], [5, 6]], [[1, 4]], [[4, 10]]]), ([])),
        (([[[1, 10]], [[4, 12]], [[4, 10]]]), ([])),
    ),
)
def test_employeeFreeTime(a, expectation):
    def fromTuple(a):
        return Interval(a[0], a[1])

    def toSchedule(a):
        for employee in a:
            yield [fromTuple(event) for event in employee]

    assert employeeFreeTime1(toSchedule(a)) == expectation
    assert employeeFreeTime2(toSchedule(a)) == expectation
