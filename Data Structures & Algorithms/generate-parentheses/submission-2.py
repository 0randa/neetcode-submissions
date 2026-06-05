class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        


        res = []
        stack = []
        def dfs(open, closed):
            
            # check for the number of open and closed parenthesis
            if open == closed == n:
                res.append("".join(stack))
                return

            if open < n:
                # add closed
                stack.append("(")
                dfs(open + 1, closed)
                stack.pop()

            if closed < open:
                # add open
                stack.append(")")
                dfs(open, closed + 1)
                stack.pop()

        dfs(0,0)
        return res

