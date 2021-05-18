from typing import List
from collections import defaultdict


def findDuplicate(paths: List[str]) -> List[List[str]]:
    """
    * 1. Imagine you are given a real file system, how will you search files? DFS or BFS?
    BFS explores neighbors first.
    This means that files which are located close to each other are also accessed one after another.
    This is great for space locality and that's why BFS is expected to be faster. Also, BFS is easier to parallelize (more fine-grained locking).
    DFS will require a lock on the root node.

    * 2. If the file content is very large (GB level), how will you modify your solution?
    For very large files we should do the following comparisons in this order:

     - compare sizes, if not equal, then files are different and stop here!
     - hash them with a fast algorithm e.g. MD5 or use SHA256 (no collisions found yet), if not equal then stop here!
     - compare byte by byte to avoid false positives due to collisions.

    * 3. If you can only read the file by 1kb each time, how will you modify your solution?
    That is the file cannot fit the whole ram.
    Use a buffer to read controlled by a loop; read until not needed or to the end.
    The sampled slices are offset by the times the buffer is called.

    * 4. What is the time complexity of your modified solution?  What is the most time-consuming part and memory consuming part of it? How to optimize?
    T = O(|num_files||sample||directory_depth|) + O(|hashmap.keys()|)

    * 5. How to make sure the duplicated files you find are not false positive?
    Add a round of final check which checks the whole string of the content.
    T = O(|num_output_list||max_list_size||file_size|).

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
