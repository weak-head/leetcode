import pytest
from problems.x_exclusive_time_of_processes import exclusive_time


@pytest.mark.parametrize(
    ("procs", "exclusive_list"),
    (
        ([[1, 150, 300], [2, 100, 200], [3, 300, 350]], [(1, 100), (2, 50), (3, 50)]),
        ([[1, 150, 400], [2, 100, 200], [3, 300, 350]], [(1, 150), (2, 50)]),
        (
            [[1, 100, 400], [2, 250, 350], [3, 100, 220], [4, 200, 250], [5, 350, 400]],
            [],
        ),
        (
            [[1, 100, 400], [2, 250, 350], [3, 100, 220], [4, 200, 250], [5, 350, 375]],
            [(1, 25)],
        ),
        (
            [[1, 100, 400], [2, 250, 350], [3, 100, 220], [4, 200, 250], [5, 360, 375]],
            [(1, 35)],
        ),
    ),
)
def test_exclusive_time(procs, exclusive_list):
    assert exclusive_time(procs) == exclusive_list
