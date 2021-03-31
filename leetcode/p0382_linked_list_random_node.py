import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getRandom(head) -> int:
    """
    Reservoir Sampling

    Covers infinite stream of data.

    Time: O(n)
    Space: O(1)
    """
    val = None
    items = 0
    while head is not None:
        # the possibility of [r == 0] is [1/items]
        if random.randint(0, items) == 0:
            val = head.val
        items += 1
        head = head.next

    return val
