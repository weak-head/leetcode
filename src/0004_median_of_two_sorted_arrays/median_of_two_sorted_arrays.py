from typing import List

def findMedianSortedArrays(a: List[int], b: List[int]) -> float:
    a_len, b_len = len(a), len(b)
    # edge cases when one of the arrays is empty
    if a_len == 0:
        return extract_single_median(b, b_len)
    if b_len == 0:
        return extract_single_median(a, a_len)

    a_lix, a_rix, b_lix, b_rix = 0, a_len - 1, 0, b_len - 1
    target_ix = (a_rix + b_rix) >> 1

    while a_lix <= a_rix or b_lix <= b_rix:
        # median of the current segment a
        a_ix_median = (a_lix + a_rix) >> 1

        # this b index provides reliable information of how much elements
        # we have from the left side in a anb b
        b_ix_match = find_index(b, b_lix, b_rix, a[a_ix_median])

        current_ix = a_ix_median + b_ix_match
        # print("current_ix: {}, target_ix: {}  [a_ix_median: {}, a_lix: {}, a_rix: {}]  [b_ix_match: {}, b_lix: {}, b_rix: {}]"
        #             .format(current_ix, target_ix, a_ix_median, a_lix, a_rix, b_ix_match, b_lix, b_rix))

        if current_ix == target_ix:
            if not (a_len + b_len) % 2:
                return extract_median(a, a_ix_median, b, b_ix_match)
            else:
                return a[a_ix_median] if a[a_ix_median] > b[b_ix_match] else b[b_ix_match]
        elif current_ix > target_ix:
            a_rix, b_rix = a_ix_median, b_ix_match

            if a_lix < a_rix and a[a_ix_median] > b[b_ix_match]:
                a_rix = a_rix - 1
            else:
                b_rix = b_rix - 1
        else:
            a_lix, b_lix = a_ix_median, b_ix_match

            if a_lix < a_rix and a[a_ix_median] < b[b_ix_match]:
                a_lix = a_lix + 1
            else:
                b_lix = b_lix + 1

def extract_median(a: List[int], a_ix_median: int, b: List[int], b_ix_median: int) -> float:
    # a contains hi-part
    if a[a_ix_median] > b[b_ix_median]:
        low_part = None
        if a_ix_median > 0:
            low_part = max(a[a_ix_median - 1], b[b_ix_median])
        else:
            low_part = b[b_ix_median]
        return (a[a_ix_median] + low_part) / 2
    # b contains hi-part
    else:
        low_part = None
        if b_ix_median > 0:
            low_part = max(b[b_ix_median - 1], a[a_ix_median])
        else:
            low_part = a[a_ix_median]
        return (b[b_ix_median] + low_part) / 2

def extract_single_median(a: List[int], a_len: int) -> float:
    median = a_len >> 1
    if a_len % 2 == 0:
        return (a[median - 1] + a[median]) / 2
    else:
        return a[median]

def find_index(l: List[int], left: int, right: int,  element: int) -> int:
    if left >= right:
        return left
    median = (left + right) >> 1
    if l[median] == element:
        return median
    elif l[median] < element:
        return find_index(l, median + 1, right, element)
    else:
        return find_index(l, left, median - 1, element)

if __name__ == '__main__':
    assert findMedianSortedArrays([], [1]) == 1
    assert findMedianSortedArrays([], [2,3,4,5,6,7,8,9,10]) == 6
    assert findMedianSortedArrays([], [1,2,3,4,5,6,7,8,9,10]) == 5.5

    assert findMedianSortedArrays([1], []) == 1
    assert findMedianSortedArrays([2,3,4,5,6,7,8,9,10], []) == 6
    assert findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10], []) == 5.5

    assert findMedianSortedArrays([1], [2]) == 1.5
    assert findMedianSortedArrays([1,2], [3,4]) == 2.5
    assert findMedianSortedArrays([1,2,3], [4,5,6]) == 3.5

    assert findMedianSortedArrays([1,3], [2]) == 2
    assert findMedianSortedArrays([1,3,5,8,9,10], [2,4,6,7,11]) == 6
    assert findMedianSortedArrays([1,3,5], [2,4,6]) == 3.5

    assert findMedianSortedArrays([1], [2,3,4,5,6,7,8,9,10,11]) == 6
    assert findMedianSortedArrays([1], [2,3,4,5,6,7,8,9,10]) == 5.5

    assert findMedianSortedArrays([2,3,4,5,6,7,8,9,10], [1]) == 5.5
    assert findMedianSortedArrays([2,3,4,5,6,7,8,9,10,11], [1]) == 6

    print('done')