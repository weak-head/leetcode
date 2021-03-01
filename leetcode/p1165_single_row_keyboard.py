def calculateTime(keyboard: str, word: str) -> int:
    """
    Time: O(n)
    Space: O(1)
        n - length of the word
    """
    m = {key: ix for ix, key in enumerate(keyboard)}  # O(1)

    total = 0
    prev = 0
    for char in word:
        loc = m[char]
        total += abs(loc - prev)
        prev = loc

    return total
