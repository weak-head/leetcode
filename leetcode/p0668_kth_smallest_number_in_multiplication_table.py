import heapq

# see also: 378


def find_kth_1(m, n, k):
    """ "
    Brute force.
    Time: O(n * m * log(n * m))
    Space: O(n * m)
    """
    matrix = [i * j for i in range(1, m + 1) for j in range(1, n + 1)]
    matrix.sort()
    return matrix[k - 1]


def find_kth_2(m, n, k):
    """
    Using Heap.
    Time: O(m * n * log m)
    Space: O(m)
    """
    heap = [(i, i) for i in range(1, m + 1)]
    heapq.heapify(heap)

    for _ in range(k):
        val, root = heapq.heappop(heap)
        nxt = val + root
        if nxt <= root * n:
            heapq.heappush(heap, (nxt, root))

    return val


def find_kth_3(m, n, k):
    """
    Binary search.
    Time: O(min(m,n) * log(m*n))
    Space: O(1)
    """

    if m > n:
        m, n = n, m

    def count_smaller_or_equal_elements(x):
        count = 0

        # for each of 'm' rows, i-th row
        # look like [1*i, 2*i, 3*i, ... , n*i]
        for i in range(1, m + 1):
            count += min(x // i, n)

        return count

    lo, hi = 1, m * n
    while lo < hi:
        mi = (lo + hi) // 2
        if count_smaller_or_equal_elements(mi) >= k:
            hi = mi
        else:
            lo = mi + 1

    return lo
