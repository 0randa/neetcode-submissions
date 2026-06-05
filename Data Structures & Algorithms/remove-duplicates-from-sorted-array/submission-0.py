class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        seen = set()

        arr_len = len(nums) - 1

        for n in nums.copy():
            # seen.add(n)
            if n in seen:
                nums.remove(n)
            else:
                seen.add(n)

        return len(nums)

        # print(len(seen))
        # return len(seen)