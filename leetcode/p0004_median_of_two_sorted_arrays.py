from typing import List


def findMedianSortedArrays(a: List[int], b: List[int]) -> float:
    a_len, b_len = len(a), len(b)
    kth_index = (a_len + b_len) >> 1
    if (a_len + b_len) % 2:
        return kth_elem(a, b, 0, a_len - 1, 0, b_len - 1, kth_index)
    else:
        kth_1 = kth_elem(a, b, 0, a_len - 1, 0, b_len - 1, kth_index - 1)
        kth_2 = kth_elem(a, b, 0, a_len - 1, 0, b_len - 1, kth_index)
        return (kth_1 + kth_2) / 2


def kth_elem(
    a: List[int],
    b: List[int],
    a_l_ix: int,
    a_r_ix: int,
    b_l_ix: int,
    b_r_ix: int,
    kth_index: int,
) -> int:
    if a_l_ix > a_r_ix:
        return b[kth_index - a_l_ix]
    if b_l_ix > b_r_ix:
        return a[kth_index - b_l_ix]

    a_m_ix = (a_l_ix + a_r_ix) >> 1
    b_m_ix = (b_l_ix + b_r_ix) >> 1
    a_m, b_m = a[a_m_ix], b[b_m_ix]

    # we are still behind the median index, we need to move forward
    if a_m_ix + b_m_ix < kth_index:
        # a_m comes before b_m
        # we need to move a_l_ix further right
        if a_m < b_m:
            return kth_elem(a, b, a_m_ix + 1, a_r_ix, b_l_ix, b_r_ix, kth_index)
        # b_m comes before a_m
        # we need to move it right
        else:
            return kth_elem(a, b, a_l_ix, a_r_ix, b_m_ix + 1, b_r_ix, kth_index)
    # we have passed the kth_index and we need to move backward
    else:
        # a_m comes after b_m
        # we need to move a_r_ix backward
        if a_m > b_m:
            return kth_elem(a, b, a_l_ix, a_m_ix - 1, b_l_ix, b_r_ix, kth_index)
        # b_m comes after a_m
        # we need
        else:
            return kth_elem(a, b, a_l_ix, a_r_ix, b_l_ix, b_m_ix - 1, kth_index)
