class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check all the rows and columns
        def check_rows():
            for row in board:
                for r in row:
                    seen = set()
                    for num in r:
                        if r == ".":
                            continue
                        
                        if r in seen:
                            return False

                        seen.add(r)
            return True

        num_rows, num_cols = len(board), len(board[0])
        def check_cols():
            for col_index in range(num_cols):
                seen = set()

                for row_index in range(num_rows):
                    # Access element at the specific row and column
                    num = board[row_index][col_index]
                    if num == ".":
                        continue
                    
                    if num in seen:
                        return False

                    seen.add(num)
            return True


        def check_sub_grids(startRow, startCol):
            seen = set()
            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    num = board[i][j]

                    if num == ".":
                        continue
                    
                    if num in seen:
                        return False

                    seen.add(num)

            return True


        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                if not check_sub_grids(i, j):
                    print("FAHH")
                    return False

        return check_rows() and check_cols()
