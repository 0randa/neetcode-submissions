class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _map = {}

        for index, num in enumerate(nums):
            # find the complement
            _map[num] = index

        for index, item in enumerate(nums):
            complement = target - item
            if _map[complement] and _map[complement] != index:
                return [_map[item], _map[complement]]

        print(_map)