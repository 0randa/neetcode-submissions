from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = {"()"}  # n=1

        for _ in range(2, n + 1):
            nxt = set()
            for s in res:
                for i in range(len(s) + 1):
                    nxt.add(s[:i] + "()" + s[i:])
            res = nxt

        return list(res)