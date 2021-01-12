from typing import List


def intervalIntersection(
    firstList: List[List[int]], secondList: List[List[int]]
) -> List[List[int]]:
    """
    Time: O(n + m)
    Space: O(n + m)
    n - number of elements in the first list
    m - number of elements in the second list
    """
    firstList.sort()
    secondList.sort()

    res = []
    i, j = 0, 0

    while i < len(firstList) and j < len(secondList):
        head = max(firstList[i][0], secondList[j][0])
        tail = min(firstList[i][1], secondList[j][1])

        if head <= tail:
            res.append([head, tail])

        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return res
