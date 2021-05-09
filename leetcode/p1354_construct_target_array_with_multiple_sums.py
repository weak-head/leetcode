from typing import List
import heapq


def isPossible(A: List[int]) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    total_sum = sum(A)
    A = [-a for a in A]  # max heap
    heapq.heapify(A)

    while True:
        max_element = -heapq.heappop(A)
        total_sum -= max_element

        if max_element == 1 or total_sum == 1:
            return True

        if max_element < total_sum or total_sum == 0 or max_element % total_sum == 0:
            return False

        # the total sum of the array could be accumulated multiple times,
        # to create this max element
        previous_element = max_element % total_sum
        total_sum += previous_element

        heapq.heappush(A, -previous_element)
