from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_dict = Counter(nums)

        most_common = freq_dict.most_common(k)

        return [x[0] for x in most_common]

        
