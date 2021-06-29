def removeDuplicates_stack(s: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    stack = []

    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return "".join(stack)


def removeDuplicates_quadratic(s: str) -> str:
    """
    Time: O(n^2)
    Space: O(n^2)
    """
    if not s:
        return s

    res = list(s)
    drop = True
    while drop and res:
        drop = False
        for i in range(1, len(res)):
            if res[i - 1] == res[i]:
                drop = True
                res[i - 1] = res[i] = "#"

        res = [c for c in res if c != "#"]

    return "".join(res)
