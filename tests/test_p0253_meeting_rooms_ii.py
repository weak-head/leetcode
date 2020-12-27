import pytest
from leetcode.p0253_meeting_rooms_ii import (
    minMeetingRooms,
    minMeetingRooms2,
    minMeetingRooms3,
)


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([(1, 10), (2, 7), (3, 19), (8, 12), (10, 20), (11, 30)], 4),
        ([], 0),
    ),
)
def test_minMeetingRooms(a, expectation):
    assert minMeetingRooms(a) == expectation
    assert minMeetingRooms2(a) == expectation
    assert minMeetingRooms3(a) == expectation
