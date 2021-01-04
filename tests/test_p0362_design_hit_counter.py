from leetcode.p0362_design_hit_counter import HitCounterBuckets


def test_HitCounter():
    hcs = [HitCounterBuckets(300)]

    for hc in hcs:
        hc.hit(1)
        hc.hit(2)
        hc.hit(3)
        assert hc.getHits(4) == 3

        hc.hit(300)
        assert hc.getHits(300) == 4
        assert hc.getHits(301) == 3
