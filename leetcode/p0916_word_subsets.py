from typing import List
from collections import Counter, defaultdict


def wordSubsets(A: List[str], B: List[str]) -> List[str]:
    """
    Time: O( max( an * max(al, bl), bn * bl ) )
    Space: O(bn * bl)
        an - number of elements in 'a'
        al - max length of the word in 'a'
        bn - number of elements in 'b'
        bl - max length of the word in 'b'
    """
    desired_state = defaultdict(int)
    for word in B:
        word_state = Counter(word)
        for k, v in word_state.items():
            desired_state[k] = max(desired_state[k], v)

    res = []
    for word in A:
        word_state = Counter(word)
        for k, v in desired_state.items():
            if k not in word_state or word_state[k] < v:
                break
        else:
            res.append(word)

    return res
