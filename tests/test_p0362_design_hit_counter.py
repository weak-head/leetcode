from leetcode.p0362_design_hit_counter import (
    HitCounterBuckets,
    HitCounterQueue,
    HitCounterQueuePair,
)


def test_HitCounter():
    hcs = [HitCounterBuckets(300), HitCounterQueue(300), HitCounterQueuePair(300)]

    for hc in hcs:
        hc.hit(1)
        hc.hit(2)
        hc.hit(2)
        hc.hit(2)
        for _ in range(500):
            hc.hit(3)
        assert hc.getHits(4) == 504

        hc.hit(300)
        assert hc.getHits(300) == 505
        assert hc.getHits(301) == 504
