import pytest
from leetcode.p0252_meeting_rooms import canAttendMeetings


@pytest.mark.parametrize(
    ("a", "expectation"),
    ((([[0, 30], [5, 10], [15, 20]]), (False)), (([[0, 1]]), (True))),
)
def test_solve(a, expectation):
    assert canAttendMeetings(a) == expectation
