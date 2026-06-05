class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "(": ")",
            "{": "}",
            "[": "]"
        }


        l,r = 0, len(s) - 1


        while l < r:
            if s[r] != mapping[s[l]]:
                return False
            l += 1
            r -= 1
        return True
