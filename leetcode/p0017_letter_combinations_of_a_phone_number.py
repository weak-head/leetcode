from typing import List

num_map = [
    [],
    [],
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["j", "k", "l"],
    ["m", "n", "o"],
    ["p", "q", "r", "s"],
    ["t", "u", "v"],
    ["w", "x", "y", "z"],
]


def letterCombinations2(digits: str) -> List[str]:
    result = []
    for digit in reversed(digits):
        if len(result) == 0:
            result = list(num_map[int(digit)])
        else:
            result = [
                char + combination
                for char in num_map[int(digit)]
                for combination in result
            ]
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

    backtrack("", digits)
    return result


def letterCombinations3(digits: str) -> List[str]:
    if not digits:
        return []

    num_map = [None, None, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def backtrack(nums):
        if len(nums) == 1:
            return num_map[int(nums[0])]

        tails = backtrack(nums[1:])

        result = []
        for char in num_map[int(nums[0])]:
            for tail in tails:
                result.append(char + tail)

        return result

    return backtrack(digits)
