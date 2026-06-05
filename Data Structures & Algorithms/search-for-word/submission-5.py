class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        if word == "":
            return True

        rows, cols = len(board), len(board[0])
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int, k: int, seen: set[tuple[int, int]]) -> bool:
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if (r, c) in seen:
                return False
            if board[r][c] != word[k]:
                return False

            # matched last character
            if k == len(word) - 1:
                return True

            seen.add((r, c))
            for dr, dc in offsets:
                if dfs(r + dr, c + dc, k + 1, seen):
                    seen.remove((r, c))  # backtrack before bubbling up success
                    return True
            seen.remove((r, c))  # backtrack on failure
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0, set()):
                    return True
        return False