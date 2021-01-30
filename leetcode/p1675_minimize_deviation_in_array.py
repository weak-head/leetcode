from typing import List
import heapq


def minimumDeviation(nums: List[int]) -> int:
    """
    Time: O(n * log(m))
    Space: O(n)
        n - number of elements in 'nums'
        m - max number in 'nums'.
            When m is power of 2, there are log(m)
            values for 'm' to process.
    """

    evens = []  # max heap
    min_value = float("inf")

    # Make sure all the numbers in max heap are 'even'
    # So we can reduce max number by 2 each time.
    for v in nums:
        if v % 2 == 0:
            min_value = min(min_value, v)
            evens.append(-v)
        else:
            min_value = min(min_value, v * 2)
            evens.append(-v * 2)

    heapq.heapify(evens)
    min_deviation = float("inf")

    # Reduce max number by 2 each time.
    # If max number is 'odd', we cant reduce more
    # and we have found our min deviation.
    while evens:
        next_max = -heapq.heappop(evens)
        min_deviation = min(min_deviation, next_max - min_value)

        if next_max % 2 == 0:
            current_value = next_max // 2
            min_value = min(min_value, current_value)
            heapq.heappush(evens, -current_value)
        else:
            # if next_max is odd,
            # we can't reduce the deviation
            break

    return min_deviation
