class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # we will have an index, and then keep incrementing it until the letters no longer match.

        first_word = strs[0]

        for i in range(len(first_word)):
            for s in strs[1:]:
                if not s:
                    return s
                if s[i] != first_word[i]:
                    return first_word[:i]

        return first_word