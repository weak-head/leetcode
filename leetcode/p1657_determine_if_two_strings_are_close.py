from collections import Counter


def closeStrings(word1: str, word2: str) -> bool:
    """
    O(n)
    n - max len of the word
    """
    # Every character that exist in 'word1' must exist in 'word2'
    if set(word1) != set(word2):
        return False

    # The frequency mapping of the two words should be the same
    frequency1 = sorted(Counter(word1).values())
    frequency2 = sorted(Counter(word2).values())
    return frequency1 == frequency2
