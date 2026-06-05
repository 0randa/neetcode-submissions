class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        new_nums = sorted(set(nums))
        

        longest_sequence = 1


        current_sequence = 1
        for i, num in enumerate(new_nums[1:]):
            # the index starts at i=0, but we initially skip the first number
            if (num - 1 == new_nums[i]):
                current_sequence += 1
            else:
                longest_sequence = max(longest_sequence, current_sequence)
                current_sequence = 1

        return max(longest_sequence, current_sequence)
