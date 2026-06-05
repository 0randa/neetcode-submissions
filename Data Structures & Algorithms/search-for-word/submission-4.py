class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        
        directions = [
            (1, 0), (0,1),(-1,0),(0,-1)
        ]
        def dfs(i, j, visited, res):
            if (min(i,j) < 0 or i >= ROWS or j >= COLS
            or (i,j) in visited):
                return False
           
            res.append(board[i][j])
            visited.add((i,j))
            
            if res == list(word):
                return True
            print(res, list(word))

            for r, c in directions:
                if dfs(i+r,j+c, visited, res):
                    return True

            res.pop()
            visited.remove((i,j))

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c, set(), []): return True

        return False