from leetcode.p0146_lru_cache import LRUCache


def test_lru():
    cache = LRUCache(4)

    assert cache.get(4) == -1

    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.put(4, 4)
    # 4 3 2 1

    cache.put(5, 5)  # overwrites 1
    assert cache.get(3) == 3  # moves 3 to top
    assert cache.get(1) == -1  # has been overwritten by 5
    # 3 5 4 2

    cache.put(6, 6)  # overwrites 2
    assert cache.get(2) == -1  # has been overwritten by 6
    # 6 3 5 4

    assert cache.get(6) == 6
    # 6 3 5 4

    cache.put(5, 5)  # moves 5 to top
    # 5 6 3 4
    cache.put(7, 7)  # overwrites 4
    # 7 5 6 3
    assert cache.get(4) == -1

    assert cache.get(7) == 7
    assert cache.get(5) == 5
    assert cache.get(6) == 6
    assert cache.get(3) == 3
    # 3 6 5 7

    cache.put(8, 8)  # overwrites 7
    # 8 3 6 5
    assert cache.get(7) == -1
    assert cache.get(5) == 5  # moves 5 to top
    # 5 8 3 6

    cache.put(9, 9)  # overwrites 6
    assert cache.get(6) == -1
    assert cache.get(9) == 9
    # 9 5 8 3

    assert cache.get(3) == 3
    assert cache.get(8) == 8
    assert cache.get(5) == 5
    assert cache.get(9) == 9
