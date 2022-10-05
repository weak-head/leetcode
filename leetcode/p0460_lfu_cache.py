from collections import defaultdict, OrderedDict


class LFUCache:
    """
    Least Frequently Used cache
    with fallback to Least Recently Used
    in case of count tie.

    The implementation is based on two maps:
      - key -> count
      - count -> OrderedDict( key -> value )

    Using the key, we can find the count.
    Using the count we have the ordered map of keys in order of addition.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity

        # key: count
        self.keyCount = defaultdict(int)

        # count : {key: value}
        self.cache = defaultdict(OrderedDict)
        self.minCount = 0

    def updateCount(self, key: int, value: int = None) -> int:
        """
        Time: O(1)
        """
        count = self.keyCount[key]
        currentVal = self.cache[count].pop(key)

        if value is not None:
            currentVal = value

        self.keyCount[key] += 1
        self.cache[count + 1][key] = currentVal

        if count == self.minCount and not self.cache[count]:
            self.minCount += 1

        return currentVal

    def get(self, key: int) -> int:
        """
        Time: O(1)
        """
        if key in self.keyCount:
            return self.updateCount(key)

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        Time: O(1)
        """
        if not self.capacity:
            return

        if key in self.keyCount:
            self.updateCount(key, value)

        else:

            # delete min count key if at max capacity
            if len(self.keyCount) == self.capacity:
                min_count_key = self.cache[self.minCount].popitem(last=False)[0]
                self.keyCount.pop(min_count_key)

            # new min count is 1
            self.minCount = 1
            self.keyCount[key] = 1
            self.cache[1][key] = value
