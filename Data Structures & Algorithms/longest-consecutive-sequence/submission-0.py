class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest_seq = 1
        nums_set = set(nums)
        nums_sorted = sorted(list(nums_set))
        print(nums_sorted)

        curr_seq = 1
        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] == nums_sorted[i - 1] + 1:
                curr_seq += 1
            else:
                if curr_seq > longest_seq:
                    longest_seq = curr_seq
        if curr_seq > longest_seq:
            longest_seq = curr_seq

        return longest_seq