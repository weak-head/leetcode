from queue import PriorityQueue
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists: List[ListNode]) -> ListNode:
    """
    Divide And Conquer

    Time: O(n * log(k))
        n - total number of nodes
        k - total number of linked lists

    """
    if not lists:
        return None

    def merge_two(l1: ListNode, l2: ListNode) -> ListNode:
        head = node = ListNode(None)

        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        node.next = l1 if l1 else l2
        return head.next

    n = len(lists)
    while n > 1:
        res = []
        for i in range(0, n, 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < n else None
            res.append(merge_two(l1, l2))
        lists, n = res, len(res)

    return lists[0]


# -----------------------------------------------
# -- Much slower solution using priority queue --


class PriorityEntry(object):
    def __init__(self, priority, data):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority


def mergeKLists_pq(lists):
    """Priority Queue"""
    head = current = ListNode(None)
    q = PriorityQueue()

    for node in lists:
        if node:
            q.put(PriorityEntry(node.val, node))

    while not q.empty():
        current.next = q.get().data
        current = current.next

        if current.next:
            q.put(PriorityEntry(current.next.val, current.next))

    return head.next
