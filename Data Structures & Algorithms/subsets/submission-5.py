class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        ans, res = [], []

        def dfs(i):

            if i >= len(nums):
                ans.append(res.copy())
                return

            
            # you have two choices


            # include nums[i]
            # append the element
            res.append(nums[i])

            # recurse
            dfs(i + 1)

            # remove element
            res.pop()
            
            # exclude nums[i]
            # after removing, branch out
            dfs(i + 1)

        dfs(0)

        return ans

