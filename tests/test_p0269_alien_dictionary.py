import pytest
from leetcode.p0269_alien_dictionary import alienOrderKahn, alienOrderDFS


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (["wrt", "wrf", "er", "ett", "rftt"], {"wertf"}),
        (["za", "zb", "ca", "cb"], {"zacb", "zabc"}),
        (["aab", "aabb", "bb"], {"ab"}),
        (["aabb", "aab", "bb"], {""}),
    ),
)
def test_alienOrder(a, expectation):
    assert alienOrderKahn(a) in expectation
    assert alienOrderDFS(a) in expectation
