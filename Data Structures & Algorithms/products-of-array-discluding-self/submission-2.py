class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if set(nums) == {0}:
            print(set(nums))
            return [0] * (len(nums))

        product = 1
        ret_list = []

        for num in nums:
            if num == 0:
                continue
            product *= num

        for num in nums:
            if 0 in nums:
                if num == 0:
                    ret_list.append(product)
                else:
                    ret_list.append(0)

            else:
                ret_list.append(int(product / num))


        return ret_list