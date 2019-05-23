nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
adds = {
    0: ("0", 0),
    1: ("1", 0),
    2: ("2", 0),
    3: ("3", 0),
    4: ("4", 0),
    5: ("5", 0),
    6: ("6", 0),
    7: ("7", 0),
    8: ("8", 0),
    9: ("9", 0),
    10: ("0", 1),
    11: ("1", 1),
    12: ("2", 1),
    13: ("3", 1),
    14: ("4", 1),
    15: ("5", 1),
    16: ("6", 1),
    17: ("7", 1),
    18: ("8", 1),
    19: ("9", 1),
}


def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    muls = build_muls(num1)
    d, result = 0, ["0"]
    for digit in reversed(num2):
        # multiplication result for this digit
        res = muls[digit].copy()

        # append the necessary number of zeroes
        # to reflect the digit power
        for _ in range(d):
            res.append("0")

        # sum the multiplication result
        result = add(res, result)
        print(num1, " * ", digit, " = ", "".join(res), "total: ", "".join(result))

        # next digit
        d = d + 1

    return "".join(result)


def build_muls(num: str) -> dict:
    muls = {"0": ["0"]}
    muls["1"] = add(num, muls["0"])
    muls["2"] = add(num, num)
    muls["3"] = add(num, muls["2"])
    muls["4"] = add(muls["2"], muls["2"])
    muls["5"] = add(muls["3"], muls["2"])
    muls["6"] = add(muls["3"], muls["3"])
    muls["7"] = add(muls["4"], muls["3"])
    muls["8"] = add(muls["4"], muls["4"])
    muls["9"] = add(muls["5"], muls["4"])
    return muls


def add(num1, num2):
    res, carry = [], 0

    num1_len, num2_len = len(num1), len(num2)
    for i in range(max(num1_len, num2_len)):
        ix1 = num1_len - i - 1
        ix2 = num2_len - i - 1
        v1 = num1[ix1] if 0 <= ix1 < num1_len else "0"
        v2 = num2[ix2] if 0 <= ix2 < num2_len else "0"

        r, carry = addc(v1, v2, carry)
        res.append(r)

    if carry:
        res.append("1")

    res.reverse()
    return res


def addc(d1: str, d2: str, carry: int) -> (str, int):
    n1, n2 = nums[d1], nums[d2]
    res = n1 + n2 + carry
    return adds[res]


# ---------------------------


def to_int(c: str) -> int:
    return ord(c) - ord("0")


def from_int(c: int) -> str:
    return chr(ord("0") + c)


def multiply2(num1: str, num2: str) -> str:
    num1_len, num2_len = len(num1), len(num2)
    res = [0] * (num1_len + num2_len)

    for ix1 in range(num1_len - 1, -1, -1):
        for ix2 in range(num2_len - 1, -1, -1):
            mul = to_int(num1[ix1]) * to_int(num2[ix2])

            rix1 = ix1 + ix2
            rix2 = rix1 + 1

            mul = mul + res[rix2]
            res[rix1] = res[rix1] + (mul // 10)
            res[rix2] = mul % 10

    sres = []
    for v in res:
        if not (len(sres) == 0 and v == 0):
            sres.append(from_int(v))

    return "".join(sres) if sres != [] else "0"
