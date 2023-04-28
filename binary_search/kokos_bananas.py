import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find max of piles
        r = max(piles)
        l = 1
        while l < r:
            rate = l + (r-l) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile/rate)
            if time > h: l = rate + 1
            else: r = rate
        return l
