class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(candidates)

        res, sol = [], []

        n = len(nums)

        def subsets(i, sol, total):
            if total == target:
                if sol not in res:
                    res.append(sol[:])

            if i >= n or total > target:
                return

            # we choose to include sol
            sol.append(nums[i])
            subsets(i + 1, sol, total + nums[i])

            # or not include
            sol.pop()
            subsets(i + 1, sol, total)

            #
        subsets(0, [], 0)
        return res
        # return res


