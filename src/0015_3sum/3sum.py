from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
        negs = [-x for x in nums if x < 0 ]
        pos  = [x for x in nums if x >= 0 ]
        zeros = [x for x in pos if x == 0 ]
        negs_set = set(negs)
        pos_set  = set(pos)
        negs_len = len(negs)
        pos_len  = len(pos)
        result = []

        # zeros edge case
        if len(zeros) >= 3:
            result.append((0,0,0))

        # double negative check
        for l1 in range(0, negs_len):
            for l2 in range(l1 + 1, negs_len):
                val = negs[l1] + negs[l2]
                if val in pos_set:
                    result.append(tuple(sorted((-negs[l1], -negs[l2], val))))
        
        # double positive check
        for r1 in range(0, pos_len):
            for r2 in range(r1 + 1, pos_len):
                val = pos[r1] + pos[r2]
                if val in negs_set:
                    result.append(tuple(sorted((-val, pos[r1], pos[r2]))))

        return list(set(result))