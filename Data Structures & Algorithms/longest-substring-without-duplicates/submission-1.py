class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # utilise a set

        l, r, longest = 0,0,0
        seen = {}
        for index, char in enumerate(s):
            
            if char not in seen:
                seen[char] = index
            else:
                print(seen)
                longest = max(r-l, longest)
                l = seen[char]
                seen[char] = index


            r += 1
        return longest - 1