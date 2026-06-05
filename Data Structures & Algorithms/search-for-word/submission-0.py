class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        res, sol = [], []

        num_rows = len(board)
        num_cols = len(board[0])

        def dfs(i, j):    
            if i < 0 or i >= num_rows or j < 0 or j >= num_cols:
                return

            sol.append(board[i][j])

            if len(sol) == len(word):
                res.append(sol[:])
                sol.pop()
                return

            # go as down as possible
            dfs(i + 1, j)
            # go right as possible
            dfs(i, j + 1)
            sol.pop()            

        for r in range(num_rows):
            for c in range(num_cols):
                dfs(r, c)

        return (list(word) in res)