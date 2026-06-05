class Solution:
    def rob(self, nums: List[int]) -> int:
        


        if len(nums) == 1:
            return nums[0]


        def opt(i, boolean):

            if i == 0:
                return nums[0]
            
            if i == 1:
                if boolean:
                    return nums[1]
                else:
                    return nums[0]


            # 2 decisions, we can rob the house, or not rob the house

            # true, then you want to rob the current house
            if boolean:
                return max(opt(i-1, True), nums[i] + opt(i-1, False))

            # false, you don't want to rob the current house
            elif not boolean:
                return max(opt(i-1, True), opt(i-1, False))

        length = len(nums) - 1
        return max(opt(length, False), opt(length,True))






        