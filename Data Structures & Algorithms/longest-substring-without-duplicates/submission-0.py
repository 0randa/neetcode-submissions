class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret_string = ""
        maxL = 0
        for char in s:
            if char in ret_string:
                idx = ret_string.index(char)
                ret_string = ret_string[idx + 1:]
            ret_string += char
            maxL = max(maxL, len(ret_string))

        print(ret_string)
        return maxL