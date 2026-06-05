class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1


        while l < r:
            mid = int((l + r) / 2)
            print(nums[mid])
            # if mid is greater, then cut the right
            if nums[mid] > target:
                r -= 1

            # if mid is less, cut the left
            elif nums[mid] < target:
                l += 1
            else:
                return mid

        return -1