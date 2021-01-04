from typing import List
from collections import defaultdict, Counter, deque


def alienOrderKahn(words: List[str]) -> str:
    """
    Based on Kahn's algorithm
    O(c)
    c - total length of all words combined
    """
    adj_list = defaultdict(set)
    in_degree = Counter({c: 0 for word in words for c in word})

    for wordA, wordB in zip(words, words[1:]):
        for chA, chB in zip(wordA, wordB):
            if chA != chB:
                if chB not in adj_list[chA]:
                    adj_list[chA].add(chB)
                    in_degree[chB] += 1
                break
        else:
            # Word B is prefix of word A
            if len(wordB) < len(wordA):
                return ""

    output = []
    no_incoming_edges = deque([v for v in in_degree if in_degree[v] == 0])
    while no_incoming_edges:
        node = no_incoming_edges.popleft()
        output.append(node)
        for to_node in adj_list[node]:
            in_degree[to_node] -= 1
            if in_degree[to_node] == 0:
                no_incoming_edges.append(to_node)

    if len(output) < len(in_degree):
        return ""

    return "".join(output)


def alienOrderDFS(words: List[str]) -> str:
    """
    Topological sort, DFS
    O(c)
    c - total length of all words combined
    """
    reverse_adj_list = {c: set() for word in words for c in word}

    for wordA, wordB in zip(words, words[1:]):
        for chA, chB in zip(wordA, wordB):
            if chA != chB:
                reverse_adj_list[chB].add(chA)
                break
        else:
            if len(wordB) < len(wordA):
                return ""

    seen = {}  # NotIn = white, False = grey, True = black
    output = []

    def visit(node):
        if node in seen:
            return seen[node]

        seen[node] = False  # grey
        for next_node in reverse_adj_list[node]:
            result = visit(next_node)
            if not result:  # was grey => cycle
                return False
        seen[node] = True  # black
        output.append(node)
        return True

    if not all(visit(node) for node in reverse_adj_list):
        return ""

    return "".join(output)
