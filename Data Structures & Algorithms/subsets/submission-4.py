class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        ans, res = [], []

        def dfs(i):

            if i >= len(nums):
                ans.append(res.copy())
                return

            # append the element
            res.append(nums[i])

            # recurse
            dfs(i + 1)

            # remove element
            res.pop()
            
            # after removing, branch out
            dfs(i + 1)

        dfs(0)

        return ans

