from typing import List
from collections import defaultdict


def findDuplicate(paths: List[str]) -> List[List[str]]:
    """
    * 1. Imagine you are given a real file system, how will you search files? DFS or BFS?
    DFS. In this case the directory path could be large.
    DFS can reuse the shared the parent directory before leaving that directory.
    But BFS cannot.

    * 2. If the file content is very large (GB level), how will you modify your solution?
    In this case, not realistic to match the whole string of the content.
    So we use file signitures to judge if two files are identical.
    Signitures can include file size, as well as sampled contents on the same positions.
    They could have different file names and time stamps though.
    Hashmaps are necessary to store the previous scanned file info.
    S = O(|keys| + |list(directory)|).
    The key and the directory strings are the main space consumption.

    a. Sample to obtain the sliced indices in the strings stored in the RAM only
        once and used for all the scanned files.
        Accessing the strings is on-the-fly.
        But transforming them to hashcode used to look up in hashmap
        and storing the keys and the directories in the hashmap can be time consuming.
        The directory string can be compressed to directory id.
        The keys are hard to compress.
    b. Use fast hashing algorithm e.g. MD5 or use SHA256 (no collisions found yet).
        If no worry about the collision, meaning the hashcode is 1-1.
        Thus in the hashmap, the storage consumption on key string can be
        replaced by key_hashcode, space usage compressed.

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
