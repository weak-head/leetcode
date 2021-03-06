from functools import lru_cache


def findCelebrity1(n: int, knows) -> int:
    """
    Time: O(n)
    Space: O(n)
    """

    @lru_cache(maxsize=None)
    def cached_knows(a, b):
        return knows(a, b)

    celebrities = set([x for x in range(n)])

    while len(celebrities) > 1:
        a = celebrities.pop()
        b = celebrities.pop()
        a_knows_b = cached_knows(a, b)

        # if 'a' knows 'b', 'a' cant be the celebrity
        if a_knows_b:
            celebrities.add(b)
        # if 'a' doesn't know 'b', 'b' cant be the celebrity
        else:
            celebrities.add(a)

    # Even if we have one potential celebrity,
    # we still don't have full confidence
    # that this person is the celebrity
    if len(celebrities) == 1:
        celebrity = celebrities.pop()
        for other in range(n):
            if celebrity == other:
                continue

            if not cached_knows(other, celebrity) or cached_knows(celebrity, other):
                return -1
        return celebrity

    return -1


def findCelebrity2(n: int, knows) -> int:
    """
    Similar to the previous approach, but less overhead

    Time: O(n)
    Space: O(1)
    """
    x = 0

    for i in range(n):
        if knows(x, i):
            x = i

    # check only [0 -> x)
    # no need to check (x -> n]
    if any(knows(x, i) for i in range(x)):
        return -1

    # check [0 -> n]
    if any(not knows(i, x) for i in range(n)):
        return -1

    return x
