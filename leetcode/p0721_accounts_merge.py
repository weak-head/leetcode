from typing import List


def accountsMerge(accounts: List[List[str]]):
    """
    Union Find / Disjoint Set

    Time: O(n * k log k)
    Space:
        n - number of accounts
        k - max number of emails belonging to the same account
    """

    parent = [i for i in range(len(accounts))]
    rank = [1] * len(accounts)

    def union(x, y):
        xp = find(x)
        yp = find(y)

        if rank[xp] < rank[yp]:
            parent[xp] = yp
        else:
            parent[yp] = xp
            if rank[xp] != rank[yp]:
                rank[xp] += 1

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    groups = {}
    for index in range(len(accounts)):
        for email in accounts[index][1:]:
            if email not in groups:
                groups[email] = index
            else:
                union(groups[email], index)

    grouped_emails = {}
    for email, index in groups.items():
        p = find(index)
        if p not in grouped_emails:
            grouped_emails[p] = [accounts[index][0]]
        grouped_emails[p].append(email)

    res = []
    for r in grouped_emails.values():
        r[1:] = sorted(r[1:])
        res.append(r)

    return res
