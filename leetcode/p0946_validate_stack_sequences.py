from typing import List


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    """
    Simulate push/pop and check
    if the resulting stack is empty in the end.

    Time: O(n)
    Space: O(n)
        n - number of pushed elements
    """
    s, i = [], 0
    for c in pushed:
        s.append(c)

        while s and s[-1] == popped[i]:
            s.pop()
            i += 1

    return len(s) == 0
