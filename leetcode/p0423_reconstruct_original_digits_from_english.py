from collections import Counter


def originalDigits(s: "str") -> "str":
    """
    The 'zwuxg' are unique letters,
    and we can use the count of them to
    identify the count of numbers:
        z - Zero (0)
        w - tWo (2)
        u - foUr (4)
        x - siX (6)
        g - eiGht (8)

    The following letters "hfs",
    could be used to identify the following numbers:
        h - tHree & eigHt (3 & 8)
        f - Five & Four (5 & 4)
        s - Seven & Six (7 & 6)

    8, 4, 6 we could get using 'zwuxg' letters that uniquely identify
    the numbers. Now we can find the 3, 5 and 7 by substracting corresponding
    counts.

    Similar logic for "in":
        i - nIne & fIve & sIx & eIght (9 & 5 & 6 & 8)
        n - oNe & NiNe & seveN (1 & 9 & 7)


    Time: O(n)
    Space: O(n)
        n - length of the 's'
    """
    count = Counter(s)

    # building hashmap digit -> its frequency
    out = {}

    # --- Unique letters ---

    # letter "z" is present only in "zero"
    out["0"] = count["z"]

    # letter "w" is present only in "two"
    out["2"] = count["w"]

    # letter "u" is present only in "four"
    out["4"] = count["u"]

    # letter "x" is present only in "six"
    out["6"] = count["x"]

    # letter "g" is present only in "eight"
    out["8"] = count["g"]

    # --- Double letters ---

    # letter "h" is present only in "three" and "eight"
    out["3"] = count["h"] - out["8"]

    # letter "f" is present only in "five" and "four"
    out["5"] = count["f"] - out["4"]

    # letter "s" is present only in "seven" and "six"
    out["7"] = count["s"] - out["6"]

    # --- Three and Four letter cases ---

    # letter "i" is present in "nine", "five", "six", and "eight"
    out["9"] = count["i"] - out["5"] - out["6"] - out["8"]

    # letter "n" is present in "one", "nine", and "seven"
    out["1"] = count["n"] - out["7"] - 2 * out["9"]

    # building output string
    output = [key * out[key] for key in sorted(out.keys())]

    return "".join(output)
