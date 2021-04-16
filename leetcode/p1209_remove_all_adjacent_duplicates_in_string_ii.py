def removeDuplicates_stack(s: str, k: int) -> str:
    """
    Compact stack

    Time: O(n)
    Space: O(n)
    """
    stack = [["#", 0]]
    for i in range(len(s)):
        if stack[-1][0] == s[i]:
            stack[-1][1] += 1
        else:
            stack.append([s[i], 1])

        if stack[-1][1] == k:
            stack.pop()

    r = [c * n for c, n in stack[1:]]
    return "".join(r)


def removeDuplicates_naive(s: str, k: int) -> str:
    """
    Naive, similar to candy crush

    Time: O((n/k) * n)
    Space: O((n/k) * n)
    """
    r = list(s)
    updated = True
    while updated:
        updated = False
        cnt = 1

        for i in range(1, len(r)):
            if r[i - 1] == r[i]:
                cnt += 1
                if cnt == k:
                    r[i - k + 1 : i + 1] = [None] * k
                    updated = True
            else:
                cnt = 1

        if updated:
            r = [v for v in r if v is not None]

    return "".join(r)
