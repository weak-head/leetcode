from queue import PriorityQueue
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists: List[ListNode]) -> ListNode:
    '''Divide And Conquer'''
    if lists == []:
        return None

    lists_len = len(lists)
    while lists_len > 1:
        res = []
        for list_ix in range(0, lists_len, 2):
            l1 = lists[list_ix]
            l2 = lists[list_ix + 1] if (list_ix + 1) < lists_len else None
            res.append(merge_two(l1, l2))
        lists = res
        lists_len = len(lists)

    return lists[0]


def merge_two(l1: ListNode, l2: ListNode) -> ListNode:
    head = node = ListNode(None)

    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next

    node.next = l1 if l1 is not None else l2
    return head.next

# -----------------------------------------------
# -- Much slower solution using priority queue --


class PriorityEntry(object):
    def __init__(self, priority, data):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority


def mergeKLists_pq(lists):
    '''Priority Queue'''
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