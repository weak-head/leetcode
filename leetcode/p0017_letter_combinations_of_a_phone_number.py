from typing import List


def letterCombinations(digits: str) -> List[str]:
    """
    Time: O(3^m * 4^n)
    Space: O(3^m * 4^n)
        m - number of digits that maps to 3 letters
        n - number of digits that maps to 4 letters
    """
    if not digits:
        return []

    m = {
        "2": "abc",
        "3": "edf",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    rs = list(m[digits[-1]])
    for d in reversed(digits[:-1]):
        rs = [v + r for v in m[d] for r in rs]

    return rs
