class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a sliding window
        l, r = 0, len(nums) - 1
        
        while l < r:
            _sum = nums[l] + nums[r]
            if _sum == target:
                return [l, r]
            elif _sum > target:
                r -= 1
            elif _sum < taget:
                l += 1

        return -1