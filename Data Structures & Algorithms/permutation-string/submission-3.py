class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) == 1 and s1 in s2:
            return True

        r = len(s1)
        for l in range(len(s2) - len(s1) - 1):
            # check if the character is in s1 set
            substring = s2[l:r]
            if Counter(substring) == Counter(s1):
                return True

            r += 1

        return False
                

