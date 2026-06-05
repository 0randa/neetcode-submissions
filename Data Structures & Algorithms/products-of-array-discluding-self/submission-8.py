class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # add a case depending on how many zeroes the array contains

        mult = 1
        numZeroes = 0
        for num in nums:
            if num != 0:
                mult *= num
            else:
                numZeroes += 1


        ans = []

        if numZeroes > 1:
            return [0] * len(nums)
        elif numZeroes == 1:
            for num in nums:
                if num != 0:
                    ans.append(0)
                else:
                    ans.append(mult)
        else:
            for num in nums:
                ans.append(mult // num)


        return ans
        
