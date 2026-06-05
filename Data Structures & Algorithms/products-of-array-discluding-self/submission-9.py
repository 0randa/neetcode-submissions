class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # add a case depending on how many zeroes the array contains

        # create a prefix and suffix array

        prefix, suffix = [1], [1]


        

        for index, num in enumerate(nums[1:], start=1):
            prefix.append(prefix[-1] * nums[index-1])


        reversed_array = nums[::-1]

        for index, num in enumerate(reversed_array[1:], start=1):
            # suffix.append(suffix[-1] * num)
            suffix.append(suffix[-1] * reversed_array[index - 1])


        ans = []
        for i, num in enumerate(prefix):
            ans.append(num * suffix[len(prefix) - i - 1])


        return ans
