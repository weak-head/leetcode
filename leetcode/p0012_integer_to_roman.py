int_to_roman_map = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def intToRoman(num: int) -> str:
    result = []
    for value, repr in int_to_roman_map:
        while num >= value:
            result.append(repr)
            num = num - value
    return "".join(result)
