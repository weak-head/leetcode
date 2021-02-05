def simplifyPath(path: str) -> str:
    """
    Time: O(n)
    Space: O(n)
        n - length of the path
    """
    s = []
    for p in path.split("/"):
        if p in {"", "."}:
            continue
        elif p == "..":
            if s:
                s.pop()
        else:
            s.append(p)
    return "/" + "/".join(s)
