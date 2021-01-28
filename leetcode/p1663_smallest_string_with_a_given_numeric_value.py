def getSmallestString(n: int, k: int) -> str:
    """
    Time: O(n)
    Space: O(n)
        n - desired length of the string
    """
    s = ["a"] * n
    k -= n
    ix = len(s) - 1

    while k > 0:
        v = min(25, k)  # from 'b' to 'z'
        s[ix] = chr(ord("a") + v)
        k -= v
        ix -= 1

    return "".join(s)


def getSmallestString2(n: int, k: int) -> str:
    """
    Time: O(1)
    Space: O(n)
        n - desired length of the string

    let there be x 'a', and z 'z' and maybe another alphabet 'y'

    case 1: no need for y
        1.x + 26.z = k
        x + z = n
        x + 26(n-x) = k
        25x = 26n-k

    case 2: y is needed and it can be from 2 to 25
        1.x + y + 26z = k
        x + z = n - 1     or      z = n - 1 - x
        x + y + 26(n - 1 - x) = k
        -25x + y + 26n - 26 - k = 0
        25x = 26n - k - 26 + y
    """

    # case 1
    if (26 * n - k) % 25 == 0:
        x = (26 * n - k) // 25
        ans = "a" * x + "z" * (n - x)
    else:  # case 2
        temp = 26 * n - k - 26
        if temp < 0:
            x = 0
            y = -temp
        else:
            y = 25 - (temp % 25)
            x = (temp + y) // 25
        ans = "a" * x + chr(ord("a") - 1 + y) + "z" * (n - 1 - x)

    return ans
