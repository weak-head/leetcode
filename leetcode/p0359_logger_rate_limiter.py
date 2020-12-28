class Logger:
    def __init__(self):
        self._history = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        last_seen = self._history.get(message, -10)
        should_print = last_seen + 10 <= timestamp
        if should_print:
            self._history[message] = timestamp
        return should_print
