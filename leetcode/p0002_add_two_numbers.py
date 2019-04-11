from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self._add_two_numbers(l1, l2, 0)

    def _add_two_numbers(self, l1: ListNode, l2: ListNode, carryover: int) -> ListNode:
        if not l1 and not l2:
            return ListNode(carryover) if carryover else None

        val = carryover
        val += l1.val if l1 else 0
        val += l2.val if l2 else 0

        n_carryover, n_val = divmod(val, 10)
        n_l1 = l1.next if l1 else None
        n_l2 = l2.next if l2 else None

        node = ListNode(n_val)
        node.next = self._add_two_numbers(n_l1, n_l2, n_carryover)

        return node

def from_array(array: List[int]) -> ListNode:
    head = node = ListNode(None)
    for el in array:
        node.next = ListNode(el)
        node = node.next
    return head.next

def to_array(node: ListNode) -> List[int]:
    res = []
    while node is not None:
        res.append(node.val)
        node = node.next
    return res

if __name__ == '__main__':
    s = Solution()

    l1 = from_array([2, 4, 3])
    l2 = from_array([5, 6, 4])
    assert to_array(s.addTwoNumbers(l1, l2)) == [7, 0, 8]

    assert s.addTwoNumbers(None, None) == None

    l1 = from_array([2, 4, 3, 1, 2, 7])
    l2 = from_array([5, 6, 4, 0, 0, 4])
    assert to_array(s.addTwoNumbers(l1, l2)) == [7, 0, 8, 1, 2, 1, 1]

    l1 = from_array([2, 4, 3])
    l2 = from_array([5, 6, 4, 0, 0, 4])
    assert to_array(s.addTwoNumbers(l1, l2)) == [7, 0, 8, 0, 0, 4]

    l2 = from_array([5, 6, 4, 0, 0, 4])
    assert to_array(s.addTwoNumbers(None, l2)) == [5, 6, 4, 0, 0, 4]

    l1 = from_array([5, 6, 4, 0, 0, 4])
    assert to_array(s.addTwoNumbers(l1, None)) == [5, 6, 4, 0, 0, 4]

    print('passed')