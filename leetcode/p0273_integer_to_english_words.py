def numberToWords(num: int) -> str:
    """
    Time: O(n)
    Space: O(1)
        n - number of digits in the number
    """
    if num == 0:
        return "Zero"

    nums = [
        ("Quintillion", 10 ** 18),
        ("Quadrillion", 10 ** 15),
        ("Trillion", 10 ** 12),
        ("Billion", 10 ** 9),
        ("Million", 10 ** 6),
        ("Thousand", 10 ** 3),
        ("Hundred", 100),
        ("Ninety", 90),
        ("Eighty", 80),
        ("Seventy", 70),
        ("Sixty", 60),
        ("Fifty", 50),
        ("Forty", 40),
        ("Thirty", 30),
        ("Twenty", 20),
        ("Nineteen", 19),
        ("Eighteen", 18),
        ("Seventeen", 17),
        ("Sixteen", 16),
        ("Fifteen", 15),
        ("Fourteen", 14),
        ("Thirteen", 13),
        ("Twelve", 12),
        ("Eleven", 11),
        ("Ten", 10),
        ("Nine", 9),
        ("Eight", 8),
        ("Seven", 7),
        ("Six", 6),
        ("Five", 5),
        ("Four", 4),
        ("Three", 3),
        ("Two", 2),
        ("One", 1),
    ]

    def ntw(num):
        for rep, val in nums:
            if val <= num:
                quotient = num // val
                remainder = num % val

                r = []

                if num >= 100:
                    r.append(ntw(quotient))

                r.append(rep)

                if remainder > 0:
                    r.append(ntw(remainder))

                return " ".join(r)

    return ntw(num)
