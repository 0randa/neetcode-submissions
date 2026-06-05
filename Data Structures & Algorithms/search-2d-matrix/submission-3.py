class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_len = len(matrix)
        row_len = len(matrix[0]) - 1

        print("matrix len is", matrix_len)
        if matrix_len == 1:
            # do binary search
            print("row_len is", row_len)
            if row_len == 0:
                print(row_len)
                if matrix[0][0] != target:
                    return False
                else:
                    return True

            l = 0
            r = row_len
            while l <= r:
                middle = (l + r) // 2

                # check if its in the row
                if matrix[0][middle] == target:
                    return True
                # compare target to the first element of the row
                elif matrix[0][middle] > target:
                    r -= 1
                elif matrix[0][middle] < target:
                    l += 1

            return False


        l = 0
        r = matrix_len - 1


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
                l += 1
