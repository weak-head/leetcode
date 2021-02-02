def atoi(s: str) -> int:
    """
    Handle leading spaces, handle sign, ignore tail,
    round by 32-bit boundary.

    Time: O(n)
    Space: O(1)
        n - length of the input string
    """
    i = 0
    while i < len(s) and s[i] == " ":
        i += 1

    if i == len(s):
        return 0

    sign = 1
    if s[i] in {"-", "+"}:
        sign = 1 if s[i] == "+" else -1
        i += 1

    val = 0
    while i < len(s) and s[i].isdigit():
        val = (val * 10) + (ord(s[i]) - ord("0"))
        i += 1

    val *= sign
    return max(-(2 ** 31), min((2 ** 31) - 1, val))
