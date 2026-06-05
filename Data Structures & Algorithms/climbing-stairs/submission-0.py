class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(i):
            if i == 0:
                return 0

            return dfs(i - 1) + 1 


        return dfs(n)
                