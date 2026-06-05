import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def can_eat(speed: int) -> bool:
            total_time = 0
            for bananas in piles:
                total_time += math.ceil(bananas / speed)
            return total_time <= h

        # binary search for the smallest speed that works
        while l < r:
            mid = (l + r) // 2
            if can_eat(mid):
                r = mid
            else:
                l = mid + 1

        return l