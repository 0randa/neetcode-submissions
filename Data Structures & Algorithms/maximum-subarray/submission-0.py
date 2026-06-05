class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        for i, num in enumerate(nums[1:]):
            if num > max_sum:
                max_sum = num
            else:
                max_sum += num

        return max_sum