class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(candidates)

        res, sol = [], []

        n = len(nums)


        # def dfs(i, sol, total):
            # if total == target:
            #     res.append(sol[:])
            #     return
            # if i >= n or total > target:
            #     return


            # if nums[i] not in sol:
            #     sol.append(nums[i])
            #     dfs(i, sol, total + nums[i])
            # else:
            #     dfs(i, sol, total)

            # sol.pop()
            # dfs(i + 1, sol, total)

        # dfs(0, [], 0)

        def subsets(i):
            if sum(sol) == target:
                if sol not in res:
                    res.append(sol[:])

            if i >= n or sum(sol) > target:
                return

            # we can choose to include it, or not include it
            sol.append(nums[i])
            subsets(i + 1)


            sol.pop()
            subsets(i + 1)

            #
        subsets(0)
        return res
        # return res


