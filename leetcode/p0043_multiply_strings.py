def multiply(num1: str, num2: str) -> str:
    """
    Generalized primary school multiplication.

    Time: O(n * m)
    Space: O(n + m)
        n - length of the first number
        m - length of the second number
    """
    r = [0] * (len(num1) + len(num2))

    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            minor = i + j + 1
            major = i + j
            res_sum = r[minor] + mul
            r[minor] = res_sum % 10
            r[major] += res_sum // 10

    # skip leading zeros
    res, i = [], 0
    while i < len(r) and r[i] == 0:
        i += 1

    for j in range(i, len(r)):
        res.append(str(r[j]))

    return "0" if not res else "".join(res)
