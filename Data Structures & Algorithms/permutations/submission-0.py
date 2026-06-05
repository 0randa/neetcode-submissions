class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(cur, visited):
            if len(cur) == n:
                res.append(cur[:])
                return
            
            # At each level, I choose one unused number 
            # and recurse deeper with that number added.
            element = None
            for num in nums:
                if not visited or num not in visited:
                    new_visited = visited.copy()
                    new_visited.add(num)

                    cur.append(num)
                    dfs(cur, new_visited)
                    cur.pop()  # backtrack

        dfs([], set())
        # print(res)
        return res
