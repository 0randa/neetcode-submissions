class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def dfs(n, res):

            if sum(res) > target or n > len(nums) - 1:
                return

            if sum(res) == target:
                ans.append(res.copy())
                return


            res.append(nums[n])

            dfs(n, res)

            res.pop()

            dfs(n + 1, res)


        dfs(0, [])

        return ans