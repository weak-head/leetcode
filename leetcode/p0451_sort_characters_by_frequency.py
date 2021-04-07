from collections import Counter
import heapq


def frequencySort_bucket(s: str) -> str:
    """
    Bucket sort

    Time: O(n)
    Space: O(n)
        n - length of the string
    """
    if not s:
        return s

    counts = Counter(s)
    max_freq = max(counts.values())
    buckets = [[] for _ in range(max_freq + 1)]

    for c, i in counts.items():
        buckets[i].append(c)

    r = []
    for i in range(len(buckets) - 1, 0, -1):
        for c in buckets[i]:
            r.append(c * i)

    return "".join(r)


def frequencySort_pq(s: str) -> str:
    """
    Priority queue

    Time: O(n + k * log k)
    Space: O(n)
        n - length of the string
        k - number of unique characters
    """
    c = Counter(s)
    h = [(-val, key) for key, val in c.items()]
    heapq.heapify(h)
    r = []
    while h:
        val, key = heapq.heappop(h)
        r.append(key * (-val))
    return "".join(r)
