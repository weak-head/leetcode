from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists: List[ListNode]) -> ListNode:
    reduced = reduce_n(lists)
    if reduced is None or reduced == []:
        return None
    return reduced[0]


def reduce_n(lists: List[ListNode]) -> List[ListNode]:
    lists_len = len(lists)
    if lists_len <= 1:
        return lists

    res = []
    for list_ix in range(0, lists_len, 2):
        l1 = lists[list_ix]
        l2 = lists[list_ix + 1] if (list_ix + 1) < lists_len else None
        res.append(merge_two(l1, l2))
    return reduce_n(res)


def merge_two(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.val > l2.val:
        l2.next = merge_two(l1, l2.next)
        return l2
    else:
        l1.next = merge_two(l1.next, l2)
        return l1

def to_list_node(l: List[int]) -> ListNode:
    head = node = ListNode(None)
    for l_ix in range(len(l)):
        node.next = ListNode(l[l_ix])
        node = node.next

    return head.next

def from_list_node(list_node: ListNode):
    while list_node is not None:
        yield list_node.val
        list_node = list_node.next


if __name__ == '__main__':
    a = to_list_node([1,4,5])
    b = to_list_node([1,3,4])
    c = to_list_node([2,6])

    abc = mergeKLists([a,b,c])
    abc_gen = from_list_node(abc)

    assert list(abc_gen) == [1,1,2,3,4,4,5,6]

    print('passed')