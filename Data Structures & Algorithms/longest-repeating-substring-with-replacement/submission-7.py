class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # we want to create a hash table, to keep track of the frequencies of each character

        num_letters = defaultdict(int)
        l = 0

        longest = 0

        for r, _char in enumerate(s):
            num_letters[_char] += 1

            most_frequent_value = max(num_letters.values())

            print(most_frequent_value)

            while (r - l) - most_frequent_value >= k:
                most_frequent_value = max(num_letters.values())
                num_letters[s[l]] = max(0, num_letters[s[l]] - 1)
                l += 1

            longest = max(longest, r - l + 1)

        return longest