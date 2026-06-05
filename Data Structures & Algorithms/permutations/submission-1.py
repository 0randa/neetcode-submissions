class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)

        def dfs(sol):
            if len(sol) == len(nums):
                res.append(sol[:])  # Make a copy of the current solution
                return

            for index in range(len(nums)):
                if not visited[index]:
                    visited[index] = True
                    sol.append(nums[index])
                    dfs(sol)
                    sol.pop()              # Backtrack
                    visited[index] = False

        dfs([])
        return res