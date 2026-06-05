class Solution:

    result = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # let's do it iterately first.

        res, sol = [], []

        n = len(nums)


        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            backtrack(i + 1)

            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()


        backtrack(0)
        return res
