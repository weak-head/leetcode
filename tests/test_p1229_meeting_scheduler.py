import pytest
from leetcode.p1229_meeting_scheduler import minAvailableDuration, minAvailableDuration2


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            (
                [
                    [216397070, 363167701],
                    [98730764, 158208909],
                    [441003187, 466254040],
                    [558239978, 678368334],
                    [683942980, 717766451],
                ],
                [
                    [50490609, 222653186],
                    [512711631, 670791418],
                    [730229023, 802410205],
                    [812553104, 891266775],
                    [230032010, 399152578],
                ],
                456085,
            ),
            ([98730764, 99186849]),
        ),
    ),
)
def test_minDuration(a, expectation):
    assert minAvailableDuration(a[0], a[1], a[2]) == expectation
    assert minAvailableDuration2(a[0], a[1], a[2]) == expectation
