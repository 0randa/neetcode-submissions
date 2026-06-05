class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
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