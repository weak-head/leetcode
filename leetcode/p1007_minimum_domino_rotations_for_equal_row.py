from typing import List


def minDominoRotations(A: List[int], B: List[int]) -> int:
    a_len, occurrences = len(A), [0] * 7

    for i in range(0, a_len):
        a_val, b_val = A[i], B[i]
        occurrences[a_val] = occurrences[a_val] + 1
        if a_val != b_val:
            occurrences[b_val] = occurrences[b_val] + 1

    max_count, max_value = 0, 0
    for i in range(1, 7):
        if occurrences[i] > max_count:
            max_count, max_value = occurrences[i], i

    if max_count < a_len:
        return -1

    swap_a, swap_b = 0, 0
    for i in range(0, a_len):
        if A[i] != max_value:
            swap_a = swap_a + 1
        if B[i] != max_value:
            swap_b = swap_b + 1

    return min(swap_a, swap_b)
