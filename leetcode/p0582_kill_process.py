from typing import List
from collections import deque, defaultdict


def killProcess(pid: List[int], ppid: List[int], kill: int) -> List[int]:
    """
    Hashtable + queue

    Time: O(n)
    Space: O(n)
        n - number of processes
    """

    m = defaultdict(list)

    for parent, child in zip(ppid, pid):
        m[parent].append(child)

    r = []
    q = deque([kill])
    while q:
        p = q.popleft()
        q.extend(m[p])
        r.append(p)

    return r
