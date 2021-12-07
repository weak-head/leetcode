class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head):
    odd_head = odd_curr = ListNode(None)
    even_head = even_curr = ListNode(None)

    i = 1
    curr = head
    while curr:
        t = curr
        if i % 2 == 0:
            even_curr.next = t
            even_curr = even_curr.next
        else:
            odd_curr.next = t
            odd_curr = odd_curr.next

        curr = curr.next
        t.next = None
        i += 1

    odd_curr.next = even_head.next
    return odd_head.next
