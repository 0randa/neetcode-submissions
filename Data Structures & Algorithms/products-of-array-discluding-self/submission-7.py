class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_without_zero = 1
        zero_count = 0

        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                product_without_zero *= n

        ans = []
        for n in nums:
            if zero_count >= 2:
                ans.append(0)
            elif zero_count == 1:
                ans.append(product_without_zero if n == 0 else 0)
            else:
                ans.append(product_without_zero // n)
        return ans