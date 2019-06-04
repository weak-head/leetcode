from bisect import insort_left, bisect_right
from collections import defaultdict, OrderedDict

# ------------------------------------------------------------


class Avl:
    class Node:
        def __init__(self, d):
            self.left = None
            self.data = d
            self.right = None
            self.heigh = 1

        def __gt__(self, other):
            return self.data > other.data

    def __init__(self):
        self._root = None

    def insert(self, v):
        self._root = self._insert(self._root, v)

    def find(self, v):
        nodes = []
        self._find(self._root, v, nodes)
        if not nodes:
            return ""
        return max(nodes).data

    def _find(self, node, v, nodes):
        if not node:
            return None

        if node.data == v:
            nodes.append(node)
            return

        if node.data < v:
            nodes.append(node)
            return self._find(node.right, v, nodes)
        else:
            return self._find(node.left, v, nodes)

    def _insert(self, node, data):
        if node is None:
            return Avl.Node(data)

        if node.data < data:
            node.right = self._insert(node.right, data)
        else:
            node.left = self._insert(node.left, data)

        return self._rebalance(node)

    def _rebalance(self, node):
        rh = self._righth(node)
        lh = self._lefth(node)

        balance = rh - lh
        if balance < -1:
            llh = self._lefth(node.left)
            lrh = self._righth(node.left)

            if llh > lrh:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        elif balance > 1:
            rlh = self._lefth(node.right)
            rrh = self._righth(node.right)

            if rrh > rlh:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        else:
            node.heigh = max(rh, lh) + 1
            return node

    def _lefth(self, node):
        return node.left.heigh if node.left else 0

    def _righth(self, node):
        return node.right.heigh if node.right else 0

    def _nodeh(self, node):
        return max(self._lefth(node), self._righth(node)) + 1

    def _rotate_left(self, node):
        x = node.right
        c3 = x.left

        node.right = c3
        x.left = node

        node.heigh = self._nodeh(node)
        x.heigh = self._nodeh(x)

        return x

    def _rotate_right(self, node):
        x = node.left
        c3 = node.right

        node.left = c3
        x.right = node

        node.heigh = self._nodeh(node)
        x.heigh = self._nodeh(x)

        return x


class TimeMapAvl:
    """
    The TimeMap using AVL tree has a lot of overhead
    and has much worse performance than TimeMap with bisect"""

    class TimeEntry:
        def __init__(self, timestamp, value):
            self.timestamp = timestamp
            self.value = value

        def __lt__(self, other):
            return self.timestamp < other.timestamp

        def __eq__(self, other):
            return self.timestamp == other.timestamp

    def __init__(self):
        self._tm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._tm:
            self._tm[key] = Avl()
        hist = self._tm[key]
        hist.insert(TimeMapAvl.TimeEntry(timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._tm:
            return ""

        hist = self._tm[key]
        te = hist.find(TimeMapAvl.TimeEntry(timestamp, None))
        if te:
            return te.value
        else:
            return ""


# ----------------------------------------------------------------------


class TimeMapBisect:
    """TimeMap that uses sorted dynamic array
    and binary search"""

    class TimeEntry:
        def __init__(self, timestamp, value):
            self.timestamp = timestamp
            self.value = value

        def __lt__(self, other):
            return self.timestamp < other.timestamp

    def __init__(self):
        self._tm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._tm:
            self._tm[key] = []
        hist = self._tm[key]
        insort_left(hist, TimeMapBisect.TimeEntry(timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._tm:
            return ""

        hist = self._tm[key]
        ix = bisect_right(hist, TimeMapBisect.TimeEntry(timestamp, None))
        if ix:
            return hist[ix - 1].value
        else:
            return ""


# ------------------------------------------------------------------------


class TimeMapListTE:
    """Optimized version of TimeMapBisect
    were we are taking advantage of the fact that the
    time sequence is strictly increasing"""

    class TimeEntry:
        def __init__(self, timestamp, value):
            self.timestamp = timestamp
            self.value = value

        def __lt__(self, other):
            return self.timestamp < other.timestamp

    def __init__(self):
        self._tm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._tm:
            self._tm[key] = []
        self._tm[key].append(TimeMapListTE.TimeEntry(timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._tm:
            return ""

        hist = self._tm[key]
        ix = bisect_right(hist, TimeMapListTE.TimeEntry(timestamp, None))
        if ix:
            return hist[ix - 1].value
        else:
            return ""


# ------------------------------------------------------------------------


class TimeMapOD:
    """Extremely slow solution using combination of
    default dictionary and ordered dictionary"""

    def __init__(self):
        self._tm = defaultdict(lambda: OrderedDict())

    def set(self, key, value, time):
        self._tm[key].update({time: value})

    def get(self, key, time):
        if key not in self._tm:
            return ""

        history = self._tm[key]
        return history.get(time, history.get(self._search(history, time), ""))

    def _search(self, history, time):
        # the source of slowness is this conversion
        # because each time we call search, we need to
        # convert the entire history to list...
        # allocate space, copy items...
        # so even we are using binary search
        # the overall time complexity is O(n)
        hist = list(history)
        print(hist)
        lix, rix = 0, len(hist) - 1
        while lix <= rix:
            mix = (lix + rix) >> 1
            if hist[mix] < time:
                lix = mix + 1
            else:
                rix = mix - 1
        return hist[rix] if rix >= 0 else ""


# ------------------------------------------------------------------------


class TimeMap:
    """The fastest solution using
    hashmap and a list of tuples
    with time and value.
    Binary search with a few optimizations"""

    def __init__(self):
        self._tm = defaultdict(lambda: list())

    def set(self, key, value, time):
        self._tm[key].append((time, value))

    def get(self, key, time):
        if key not in self._tm:
            return ""

        hist = self._tm[key]
        lx, rx = 0, len(hist) - 1

        if hist[lx][0] > time:
            return ""

        if hist[rx][0] < time:
            return hist[rx][1]

        while lx <= rx:
            mx = (lx + rx) >> 1
            mx_time = hist[mx][0]
            if mx_time == time:
                return hist[mx][1]
            elif mx_time < time:
                lx = mx + 1
            else:
                rx = mx - 1

        return hist[rx][1]
