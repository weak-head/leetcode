import pytest
from leetcode.p0043_multiply_strings import (
    multiply,
    multiply2,
    multiply3,
    add,
    build_muls,
)


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
    ),
)
def test_multipy(a, b, expectation):
    assert multiply(a, b) == expectation
    assert multiply2(a, b) == expectation
    assert multiply3(a, b) == expectation


@pytest.mark.parametrize(
    ("a", "b", "result"),
    (
        ("123", "0", ["1", "2", "3"]),
        ("0", "123", ["1", "2", "3"]),
        ("999", "1", ["1", "0", "0", "0"]),
        ("998", "1", ["9", "9", "9"]),
        ("0", "0", ["0"]),
        ("12345", "67890", ["8", "0", "2", "3", "5"]),
        ("999", "1001", ["2", "0", "0", "0"]),
        ("999", "11001", ["1", "2", "0", "0", "0"]),
    ),
)
def test_add(a, b, result):
    assert add(a, b) == result


@pytest.mark.parametrize(
    ("a", "muls"),
    (
        (
            "11",
            {
                "0": "0",
                "1": "11",
                "2": "22",
                "3": "33",
                "4": "44",
                "5": "55",
                "6": "66",
                "7": "77",
                "8": "88",
                "9": "99",
            },
        ),
    ),
)
def test_muls(a, muls):
    build_muls(a) == muls