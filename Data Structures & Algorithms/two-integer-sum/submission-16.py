class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}        

        for i, num in enumerate(nums):
            _dict[num] = i


        for i, num in enumerate(nums):
            difference = target - num
            
            if difference in _dict:
                return [i, _dict[difference]]
