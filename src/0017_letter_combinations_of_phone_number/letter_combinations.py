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

def letterCombinations(digits: str) -> List[str]:
    result = []
    for digit in reversed(digits):
        if len(result) == 0:
            result = list(num_map[int(digit)])
        else:
            result = [char + combination for char in num_map[int(digit)] for combination in result]
    return result

if __name__ == '__main__':
    assert letterCombinations('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    print('passed')