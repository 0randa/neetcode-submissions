class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []


        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }


        res, ans = "", []

        def dfs(i):
            nonlocal res
            if i == len(digits):
                if len(res) == len(digits):
                    ans.append(str(res))
                return

            # choice 1: include the letter
            
            for l in mapping[digits[i]]:
                res += l

                dfs(i + 1)

                res = res[:-1]

            # choice 2: don't include it    
            dfs(i + 1)

        dfs(0)
        return ans