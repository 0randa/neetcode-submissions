class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1

        contains_zero = False

        for num in nums:
            if num != 0:
                product *= num
            else:
                contains_zero = True

        _list = []

        for n in nums:
            if n == 0:
                _list.append(product)
            elif contains_zero:
                _list.append(0)
            else:
                _list.append(int(product / n))

        return _list