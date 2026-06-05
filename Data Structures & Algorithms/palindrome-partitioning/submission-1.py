class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans, res = [], []

        def is_palindrome(_str):
            return _str == _str[::-1]



        def dfs(i, j):
            
            if j >= len(s):
                if i == j:
                    ans.append(res.copy())
                return

            # we can either

            # partition and start a new string

            if (is_palindrome(s[i:j+1])):
                res.append(s[i:j+1])

                dfs(j + 1, j + 1)

                res.pop()


            dfs(i, j + 1)


            # continue without partitioning




        dfs(0, 0)
        return ans