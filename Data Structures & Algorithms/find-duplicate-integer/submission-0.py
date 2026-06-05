class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for num in nums:

            if nums[num-1] == 0:
                return num
            else:
                nums[num-1] == 0