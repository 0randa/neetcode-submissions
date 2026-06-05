class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        new_nums = set(nums)
        
        longest_sequence = 1
        current_sequence = 1
        for num in nums:
            if num - 1 not in new_nums:
                # create a sequence
                current_sequence = 1

                while num + current_sequence in new_nums:
                    current_sequence += 1

                longest_sequence = max(longest_sequence, current_sequence)



        return max(longest_sequence, current_sequence)
