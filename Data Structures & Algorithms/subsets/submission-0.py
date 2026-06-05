class Solution:


    def subsets(self, nums: List[int]) -> List[List[int]]:
        # let's do it iterately first.
        retset = [[]]
        # iterate through the input list
        for num in nums:
            for _set in retset.copy():
                copy = _set.copy()
                copy.append(num)
                retset.append(copy)

        return retset
