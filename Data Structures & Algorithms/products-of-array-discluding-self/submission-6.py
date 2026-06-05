class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        def get_product(index):
            product = 1
            for i, num in enumerate(nums):
                if i == index:
                    continue
                product *= num

            return product

        ans = []
        for i, num in enumerate(nums):
            prod = get_product(i)
            ans.append(prod)

        return ans
        