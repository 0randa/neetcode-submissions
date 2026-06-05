class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for num in nums:
            print(num, nums[num-1])
            if nums[num-1] == 0:
                return num
            else:
                nums[num-1] = 0