def isValid(s: str) -> bool:
    open_map = {"(": ")", "{": "}", "[": "]"}
    close_map = {")", "}", "]"}
    stack = []
    for char in s:
        if char in open_map:
            stack.append(open_map[char])
        elif char in close_map:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if top != char:
                return False
    return len(stack) == 0


def isValid2(s: str) -> bool:
    stack = []
    for c in s:
        if c in {"(", "{", "["}:
            stack.append(c)
        elif c in {")", "}", "]"}:
            if not stack:
                return False
            p = stack.pop()
            if (p, c) not in {("(", ")"), ("{", "}"), ("[", "]")}:
                return False
    return not stack
