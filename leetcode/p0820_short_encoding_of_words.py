from typing import List


def minimumLengthEncoding_set(words: List[str]) -> int:
    """
    Create set of words,
    Discard all suffixes from the set.
    The left words are the minimal encoding.

    Time: O(n * m)
    Space: O(n * m)
        n - number of words
        m - max length of the word
    """
    s = set(words)
    for word in words:
        for start in range(1, len(word)):
            suffix = word[start:]
            s.discard(suffix)
    return sum(map(lambda x: len(x) + 1, s))


def minimumLengthEncoding_trie(words: List[str]) -> int:
    """
    Build trie from the reversed strings
    and count the number of leaves

    We reverse the words:
        [ time, me, bell ] -> [ emit, em, lleb ]
    To build the trie

    Time: O(n * m)
    Space: O(n * m)
        n - number of words
        m - max length of the words
    """
    trie = {}

    # create trie
    for word in words:
        node = trie
        for i in range(len(word) - 1, -1, -1):
            node = node.setdefault(word[i], {})

    # get count
    def traverse(node, depth):
        if not node:
            return depth + 1  # extra char for ending
        return sum([traverse(child, depth + 1) for child in node.values()])

    return traverse(trie, 0)


def minimumLengthEncoding_substr(words: List[str]) -> int:
    """
    Naive solution,
    sort by len and compose encoding.

    Time: O( (n * log(n)) + (n * l) )
    Space: O(l)
        n - number of words
        l - length of the encoded string
    """
    words.sort(key=len, reverse=True)
    s = ""
    for word in words:
        we = word + "#"
        if s.find(we) == -1:
            s += we
    return len(s)
