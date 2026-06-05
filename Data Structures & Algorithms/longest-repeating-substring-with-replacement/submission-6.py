class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0

        _Counter = defaultdict(int)



        longest = 1

        for r in range(len(s)):
            _Counter[s[r]] += 1

            # 
            max_key = max(_Counter.values())
            
            # check that length of a string - max_key >= k

            while (r - l + 1) -  max_key > k:
                _Counter[s[l]] -= 1
                l += 1
                max_key = max(_Counter.values())


            longest = max(longest, r - l + 1)


        return longest

