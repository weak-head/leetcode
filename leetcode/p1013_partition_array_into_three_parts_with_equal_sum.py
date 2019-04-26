from typing import List

def canThreePartsEqualSum(A: List[int]) -> bool:
    if len(A) < 3:
        return False

    (q, r) = divmod(sum(A), 3)
    if r != 0:
        return False

    n, part_sum = 0, 0
    for x in A:
        # print(x)
        part_sum = part_sum + x
        if part_sum == q:
            # print(part_sum, '==', q)
            n = n + 1
            part_sum = 0

    return (n == 3) or (n > 3 and q == 0)