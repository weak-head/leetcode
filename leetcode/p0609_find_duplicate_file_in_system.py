from typing import List
from collections import defaultdict


def findDuplicate(paths: List[str]) -> List[List[str]]:
    """
    Time: O(n * s)
    Space: O(n * s)
        n - total number of files across all paths
        s - average file content size
    """

    def extract(file_info):
        ix = file_info.find("(")
        file_name = file_info[:ix]
        content = file_info[ix + 1 : -1]
        return file_name, content

    files = defaultdict(set)

    for path in paths:
        info = path.split()
        folder = info[0]
        for file_info in info[1:]:
            file_name, content = extract(file_info)

            file_path = f"{folder}/{file_name}"
            files[content].add(file_path)

    res = []
    for content, duplicates in files.items():
        if len(duplicates) > 1:
            res.append(duplicates)

    return res
