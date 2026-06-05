class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # logic is start at the middle

        l, r = 0, len(matrix) - 1
        

        row_len = len(matrix[0]) - 1

        
        
        while l <= r:
            mid = math.floor(l + r / 2)

            # compare the target

            first_num, last_num = matrix[mid][0], matrix[mid][row_len]

            
            # target is larger, then decrement the right counter
            if target > first_num and target > last_num:
                l = mid + 1
            # target is smaller, increment the left counter
            elif target < first_num and target < last_num:
                r = mid - 1
            else:
                # then do binary search

                l2, r2 = 0, row_len

                possible_row = matrix[mid]

                while l2 <= r2:
                    mid2 = math.floor((l2 + r2) / 2)
                    
                    # less than target
                    if possible_row[mid2] < target:
                        l2 = mid2 + 1
                    # greater than target
                    elif possible_row[mid2] > target:
                        r2 = mid2 - 1
                    else:
                        return True
                

                return False


                print(matrix[mid])
                break

        return False


