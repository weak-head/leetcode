import pytest
from leetcode.p0038_count_and_say import countAndSay


@pytest.mark.parametrize(
    ("a", "expectation"), ((1, "1"), (2, "11"), (3, "21"), (4, "1211"), (5, "111221"))
)
def test_countAndSay(a, expectation):
    assert countAndSay(a) == expectation
