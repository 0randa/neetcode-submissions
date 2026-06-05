class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # keep a sliding window of size k


        # compare the first element and last element

        # if the last element is closer than the first element, then maybe you should increment

        l, r = 0, k

        def get_closeness(x, y):
            return abs(x- y)

        while r < len(arr) - 1:
            print(arr[l:r])

            close_l = get_closeness(x, arr[r])
            close_r = get_closeness(x, arr[r])

            # also get the closeness of the next element

            close_rp1 = get_closeness(x, arr[r+1])

            if close_rp1 >= close_l:
                l += 1
                r += 1
            else:
                break

            
        return arr[l:r]