class Solution:
    def search(self, nums: List[int], target: int) -> int:
        arr_len = len(nums)
        l, r = 0, arr_len - 1

        while l <= r:
            middle = (l + r) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                l = middle + 1
            elif nums[middle] > target:
                r = middle - 1

        return -1
