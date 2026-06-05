class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # iterate through the array backwards
        original_length = len(nums)

        for index, num in enumerate(nums[::-1]):
            real_index = original_length - index - 1
            if num == val:
                # print(index, num)
                nums.pop(real_index)


        return len(nums)