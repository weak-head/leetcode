class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode_math(headA: ListNode, headB: ListNode) -> ListNode:
    """
    If there is an intersection of A and B,
    then we know that the length of A is a + c,
    and the length of B is b + c, where:
        a - length of A head
        b - length of B head
        c - length of A/B intersection

    So we can use this property, to traverse the
    A and B at the same time, to find the intersection.

    For example we have two lists:
        A -> [1 2 9 a b]
        B -> [1 2 3 4 5 6 7 8 9 a b]
    where intersection is: [9 a b]

        A length = 2 + 3
        B length = 8 + 3

    Traverse A and B at the same time while A or B are not none
        a -> [1 2 9 a b] => None
        b -> [1 2 3 4 5] => [6 7 8 9 a b]

    Let A point to B head:
        a -> [1 2 3 4 5 6 7 8 9 a b]
        b -> [6 7 8 9 a b]

    Keep traversing:
        a -> [1 2 3 4 5 6] => [7 8 9 a b]
        b -> [6 7 8 9 a b] => None

    Let B point to A head:
        a -> [7 8 9 a b]
        b -> [1 2 9 a b]

    Keep traversing:
        a -> [7 8] => [9 a b]
        b -> [1 2] => [9 a b]

    If there is no intersection,
    on the second iteration
    both pointers would be None.

    Time: O(n + m)
    Space: O(1)
        n - length of A
        m - length of B
    """

    pA, pB = headA, headB
    while pA != pB:
        pA = headB if pA is None else pA.next
        pB = headA if pB is None else pB.next

    return pA


def getIntersectionNode_fastslow(headA: ListNode, headB: ListNode) -> ListNode:
    """
    - Create cycle in A.
    - Detect cycle in B.
    - If there is a cycle in B, find the start of the cycle

    Slow, complex and not efficient.

    Time: O(n + m)
    Space: O(1)
        n - length of A
        m - length of B
    """
    if headA is None or headB is None:
        return None

    tailA = headA
    while tailA.next is not None:
        tailA = tailA.next

    # create cycle in A
    tailA.next = headA

    # detect cycle in B
    fastB = slowB = headB
    while fastB and fastB.next:
        slowB = slowB.next
        fastB = fastB.next.next
        if fastB == slowB:
            break

    # no cycle in B
    if fastB is None or fastB.next is None:
        tailA.next = None
        return None

    # detect start of the cycle
    slowB = headB
    while fastB != slowB:
        fastB = fastB.next
        slowB = slowB.next

    tailA.next = None
    return fastB
