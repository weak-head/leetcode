import pytest
from leetcode.p0043_multiply_strings import multiply


@pytest.mark.parametrize(
    ("a", "b", "expectation"),
    (
        ("0", "0", "0"),
        ("0", "102", "0"),
        ("111", "0", "0"),
        ("10", "10", "100"),
        ("40", "40", "1600"),
        ("592", "943", "558256"),
        ("1234567890", "987654321", "1219326311126352690"),
        ("5938238512", "392839592090301935", "2332775194789001532125120720"),
        (
            "2934293479237492783492374927345938238512",
            "723894729347392839592090301935",
            "2124119583978444509094535306984539867031889677545823075404432125120720",
        ),
        ("0", "392839592090301935", "0"),
        ("5938238512", "0", "0"),
    ),
)
def test_multipy(a, b, expectation):
    assert multiply(a, b) == expectation
