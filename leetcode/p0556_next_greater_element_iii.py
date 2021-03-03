def nextGreaterElement(n: int) -> int:
    """
    Next perumation

    Time: O(n)
    Space: O(n)
        n - number of digits
    """
    num = list(str(n))

    i = len(num) - 1
    while i > 0 and num[i - 1] >= num[i]:
        i -= 1

    if i == 0:
        return -1

    k, j = i - 1, i + 1
    while j < len(num) and num[j] > num[k]:
        j += 1

    num[k], num[j - 1] = num[j - 1], num[k]

    j = len(num) - 1
    while i < j:
        num[i], num[j] = num[j], num[i]
        i += 1
        j -= 1

    num = int("".join(num))
    num = -1 if num > 2 ** 31 - 1 else num
    return num
