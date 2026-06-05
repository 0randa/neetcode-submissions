class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        _counter = Counter()
        l,r = 0, 0
        longest = 0
        for c in s:
            sub_string = s[l:r+1]
            _counter = Counter(sub_string)
            most_common, freq = _counter.most_common(1)[0]
            curr_length = len(sub_string)

            can_be_replaced = curr_length - freq

            if can_be_replaced > k:
                l += 1
            else:
                longest = max(r - l + 1, longest)
            r += 1

        return longest