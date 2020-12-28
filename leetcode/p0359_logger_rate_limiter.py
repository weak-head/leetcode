from collections import deque


class Logger:
    def __init__(self):
        self._history = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        last_seen = self._history.get(message, -10)
        should_print = last_seen + 10 <= timestamp
        if should_print:
            self._history[message] = timestamp
        return should_print


class Logger2:
    def __init__(self):
        self._msg_set = set()
        self._msg_queue = deque()

    def shouldPrintMessage(self, timestamp, message):
        while self._msg_queue:
            msg, ts = self._msg_queue[0]
            if timestamp - ts >= 10:
                self._msg_queue.popleft()
                self._msg_set.remove(msg)
            else:
                break

        if message not in self._msg_set:
            self._msg_set.add(message)
            self._msg_queue.append((message, timestamp))
            return True
        else:
            return False
