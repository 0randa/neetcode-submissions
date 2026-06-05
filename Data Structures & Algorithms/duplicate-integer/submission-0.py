class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in reversed(nums):
            nums.pop()

            if num in nums:
                return True

        return False