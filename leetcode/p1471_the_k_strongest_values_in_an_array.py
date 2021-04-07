import heapq
import random
from typing import List


def getStrongest_sort(arr: List[int], k: int) -> List[int]:
    """
    Sort and use two pointers.

    Time: O(n * log n)
    Space: O(n)
    """
    arr.sort()
    median = arr[(len(arr) - 1) // 2]
    res = []
    l, r = 0, len(arr) - 1
    while len(res) < k:
        if abs(arr[l] - median) > abs(arr[r] - median):
            res.append(arr[l])
            l += 1
        else:
            res.append(arr[r])
            r -= 1
    return res


def getStrongest_quickselect(arr: List[int], k: int) -> List[int]:
    """
    Find median using quickselect.
    Compose weights using median.
    Use priority queue to keep k strongest weights.

    Average Time: O(n * log k)
    Worst Time: O(n^2)
    Space: O(n)
    """

    def quickselect(arr, n):
        """
        Average Time: O(n)
        Worst Time: O(n^2)
        """

        def partition(l, r):
            m = random.randint(l, r)
            arr[r], arr[m] = arr[m], arr[r]

            for i in range(l, r):
                if arr[i] <= arr[r]:
                    arr[l], arr[i] = arr[i], arr[l]
                    l += 1

            arr[l], arr[r] = arr[r], arr[l]
            return l

        def kth(l, r):
            pivot = partition(l, r)
            if pivot == n:
                return arr[n]
            elif n < pivot:
                return kth(l, pivot - 1)
            else:
                return kth(pivot + 1, r)

        return kth(0, len(arr) - 1)

    median = quickselect(arr, (len(arr) - 1) // 2)
    pq = []
    for value in arr:
        heapq.heappush(pq, (abs(value - median), value))
        if len(pq) > k:
            heapq.heappop(pq)

    return [v[1] for v in pq]
