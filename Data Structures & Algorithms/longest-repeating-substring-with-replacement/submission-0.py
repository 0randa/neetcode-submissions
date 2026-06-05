class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        
        longest = 0
        while r < len(s):
            letter_count = Counter(s[l:r+1])
            print(letter_count)
            summ = 0
            for element, count in list(letter_count.most_common())[1:]:
                summ += count

            if summ == k:
                longest = max(longest, summ + letter_count.most_common()[0][1])
            r += 1

        return longest