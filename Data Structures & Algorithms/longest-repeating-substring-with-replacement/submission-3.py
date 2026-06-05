class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        
        letter_count = Counter(s)
        if len(letter_count) == 1:
            return len(s)

        longest = 0
        for r in range(len(s)):
            letter_count = Counter(s[l:r+1])
            print(letter_count)
            summ = 0
            for element, count in list(letter_count.most_common())[1:]:
                summ += count

            if summ <= k:
                longest = max(longest, summ + letter_count.most_common()[0][1])
            else:
                l += 1

        return longest