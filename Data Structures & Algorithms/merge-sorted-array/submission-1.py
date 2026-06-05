class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        length = m + n - 1

        # loop through the nums1 array, then find the first element that is smaller than the curr element in nums2

        for number in nums2:
            for idx, n1 in enumerate(nums1):
                # print(idx, n1)
                # find the first number in nums1 that is greater than nums2
                if n1 > number:
                    # print(range(n1, len(nums1)))
                    print("hey")
                    for i in reversed(range(idx, len(nums1))):
                        nums1[i] = nums1[i-1]
                        # print(i)

                    nums1[idx] = number
                    break
                # we are at the last n elements
 
                elif len(nums1) - idx <= n and number > nums1[idx - 1] and nums1[idx] == 0:
                    nums1[idx] = number
                    break



