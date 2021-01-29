from functools import lru_cache


def findCelebrity(n: int, knows) -> int:
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

            #
            if not cached_knows(other, celebrity) or cached_knows(celebrity, other):
                return -1
        return celebrity

    return -1
