from typing import List

num_map = [
    [],
    [],
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o'],
    ['p', 'q', 'r', 's'],
    ['t', 'u', 'v'],
    ['w', 'x', 'y', 'z']
]


def letterCombinations2(digits: str) -> List[str]:
    result = []
    for digit in reversed(digits):
        if len(result) == 0:
            result = list(num_map[int(digit)])
        else:
            result = [
                char + combination for char in num_map[int(digit)] for combination in result]
    return result

# backtracking


def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []

    result = []

    def backtrack(combination: str, next_digits: str):
        if len(next_digits) == 0:
            result.append(combination)
            return
        for char in num_map[int(next_digits[0])]:
            backtrack(combination + char, next_digits[1:])

    backtrack('', digits)
    return result


if __name__ == '__main__':
    assert letterCombinations(
        '23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    print('passed')
