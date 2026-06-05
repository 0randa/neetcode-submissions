class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}        

        for i, num in enumerate(nums):
            _dict[num] = i

        # print the dictionary
        print(_dict)


        for i, num in enumerate(nums):
            difference = target - num
            if difference in _dict and (i != _dict[difference]):
                return [i, _dict[difference]]
