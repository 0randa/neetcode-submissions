from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k  # window is arr[l:r]

        while r < len(arr):
            # Compare leftmost element in current window
            # with the next candidate on the right
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
                r += 1
            else:
                break

        return arr[l:r]