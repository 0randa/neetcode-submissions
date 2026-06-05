from typing import List
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def opt(i: int) -> int:
            if i < 0:
                return 0
            if i == 0:
                return nums[0]

            return max(opt(i - 1), nums[i] + opt(i - 2))

        return opt(len(nums) - 1)