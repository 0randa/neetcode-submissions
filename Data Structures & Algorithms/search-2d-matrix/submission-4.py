class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_len = len(matrix)
        row_len = len(matrix[0])

        # Binary search on rows
        l, r = 0, matrix_len - 1
        while l <= r:
            middle = (l + r) // 2

            # Check if target is within the current row's range
            if matrix[middle][0] <= target <= matrix[middle][row_len - 1]:
                # Perform binary search within this row
                row = matrix[middle]
                l_row, r_row = 0, row_len - 1
                while l_row <= r_row:
                    mid_row = (l_row + r_row) // 2
                    if row[mid_row] == target:
                        return True
                    elif row[mid_row] < target:
                        l_row = mid_row + 1
                    else:
                        r_row = mid_row - 1
                return False  # Target not found in the row
            elif matrix[middle][0] > target:
                r = middle - 1
            else:
                l = middle + 1

        return False  # Target not found