class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        ans, res = set(), []


        def dfs(i, currSum):
            if currSum == target:
                ans.add(tuple(res.copy()))
                return
            
            if i >= len(candidates):
                return

            # 2 choices

            # i) include i
            res.append(candidates[i])

            dfs(i + 1, currSum + candidates[i])

            res.pop()

            # while (candidates[i] == candidates[i - 1]):
                # i += 1

            dfs(i + 1, currSum)
            # ii) don't include it, and move on to the next index
            
        dfs(0, 0)


        # create a set, and then return the answer
        return [list(x) for x in ans]
