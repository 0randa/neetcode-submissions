class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums) - 1
        
        while l < r:
            # less than the target, then we want a larger number
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                return [l, r]