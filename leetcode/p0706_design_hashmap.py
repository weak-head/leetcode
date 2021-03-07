class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Bucket:
    """
    There are multiple ways how to implement the bucket.
    Here we use linked list for constant remove time.
    """

    def __init__(self):
        self.head = ListNode(None, None)

    def put(self, key, value):
        prev, cur = self.head, self.head.next
        while cur:
            if cur.key == key:
                cur.value = value
                return
            prev = cur
            cur = cur.next
        prev.next = ListNode(key, value)

    def get(self, key):
        node = self.head.next
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key):
        prev, cur = self.head, self.head.next
        while cur:
            if cur.key == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next


class MyHashMap:
    def __init__(self):
        self.size = 4019  # prime
        self.m = [None] * self.size

    def put(self, key: int, value: int) -> None:
        """
        Time: O(1) # amortized
        """
        key_hash = self._hash(key)
        self.m[key_hash].put(key, value)

    def get(self, key: int) -> int:
        """
        Time: O(1) # amortized
        """
        key_hash = self._hash(key)
        return self.m[key_hash].get(key)

    def remove(self, key: int) -> None:
        """
        Time: O(1) # amortized
        """
        key_hash = self._hash(key)
        self.m[key_hash].remove(key)

    def _hash(self, key: int) -> int:
        h = key % self.size
        # lazy bucket creation
        if self.m[h] is None:
            self.m[h] = Bucket()
        return h
