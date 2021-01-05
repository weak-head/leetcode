import pytest
from leetcode.p0759_employee_free_time import (
    Interval,
    employeeFreeTime1,
    employeeFreeTime2,
    employeeFreeTime3,
)


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]), ([(3, 4)])),
        (([[[1, 2], [5, 6], [8, 10]], [[1, 3]], [[4, 6]]]), ([(3, 4), (6, 8)])),
        (([[[1, 2], [5, 6]], [[1, 4]], [[4, 10]]]), ([])),
        (([[[1, 10]], [[4, 12]], [[4, 10]]]), ([])),
    ),
)
def test_employeeFreeTime(a, expectation):
    def toSchedule(a):
        return [[Interval(event[0], event[1]) for event in empl] for empl in a]

    assert employeeFreeTime1(toSchedule(a)) == expectation
    assert employeeFreeTime2(toSchedule(a)) == expectation
    assert employeeFreeTime3(toSchedule(a)) == expectation
