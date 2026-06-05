class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # utilise a set
        if len(s) == 1:
            return 1

        l, r, longest = 0,0,0
        seen = {}
        for index, char in enumerate(s):
            
            if char not in seen:
                seen[char] = index
            else:
                print(seen)
                longest = max(r-l - 1, longest)
                l = seen[char]
                seen[char] = index


            r += 1
        return longest