class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        row_len = len(matrix[0]) - 1

        while l <= r:
            middle = (l + r) // 2

            # check if its in the row
            if matrix[middle][0] <= target <= matrix[middle][row_len]:
                if target in matrix[middle]:
                    return True
                else: 
                    return False

            # compare target to the first element of the row
            elif matrix[middle][0] > target:
                r -= 1
            elif matrix[middle][0] < target:
                l -=1
