from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows and columns for duplicates
        if not self.check_duplicates(board):
            return False

        # Check each 3x3 subgrid for duplicates
        for start_row in range(0, 9, 3):  # 0, 3, 6
            for start_col in range(0, 9, 3):  # 0, 3, 6
                if not self.check_subgrid(board, start_row, start_col):
                    return False

        return True

    def check_duplicates(self, board: List[List[str]]) -> bool:
        # Check rows for duplicates
        for row in board:
            row_set = set()
            for cell in row:
                if cell.isnumeric():
                    if cell in row_set:
                        return False
                    row_set.add(cell)

        # Check columns for duplicates
        for col in range(len(board[0])):
            col_set = set()
            for row in board:
                if row[col].isnumeric():
                    if row[col] in col_set:
                        return False
                    col_set.add(row[col])

        return True

    def check_subgrid(self, board: List[List[str]], start_row: int, start_col: int) -> bool:
        # Check a single 3x3 subgrid for duplicates
        subgrid_set = set()
        for row in range(start_row, start_row + 3):
            for col in range(start_col, start_col + 3):
                if board[row][col].isnumeric():
                    if board[row][col] in subgrid_set:
                        return False
                    subgrid_set.add(board[row][col])

        return True