import pytest
from leetcode.p0269_alien_dictionary import alienOrderKahn


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
        (["za", "zb", "ca", "cb"], "zacb"),
        (["aab", "aabb", "bb"], "ab"),
        (["aabb", "aab", "bb"], ""),
    ),
)
def test_alienOrder(a, expectation):
    assert alienOrderKahn(a) == expectation
