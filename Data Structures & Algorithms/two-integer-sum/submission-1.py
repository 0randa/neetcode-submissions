class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            index = nums.index(target - nums[i], i + 1)

            if index:
                return [i, index]

        return -1