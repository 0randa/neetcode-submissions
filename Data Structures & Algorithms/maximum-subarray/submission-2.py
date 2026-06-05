class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)

        max_sum = nums[0]
        for i in range(length):
            for j in range(i, length):
                max_sum = max(sum(nums[i:j + 1]), max_sum)

        # max_sum = nums[0]
        # for i, num in enumerate(nums[1:]):
        #     # start a new subarray
        #     if num > max_sum:
        #         max_sum = num
        #     # continue with it.
        #     else:
        #         max_sum += num

        return max_sum