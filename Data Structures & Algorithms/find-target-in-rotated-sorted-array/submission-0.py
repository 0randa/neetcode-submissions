class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            minn = min(abs(nums[l] - target), abs(nums[r] - target))
            if abs(nums[l] - target) == minn:
                r = mid
            elif abs(nums[r] - target) == minn:
                l = mid


        return -1