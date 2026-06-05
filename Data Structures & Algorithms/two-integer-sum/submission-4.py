class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):

            if target - nums[i] in nums:
                index = nums.index(target - nums[i], i + 1)
                return [i, index]

        return -1