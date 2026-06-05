class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) == 1 and s1 in s2:
            return True

        l = 0
        for r in range(len(s2)):
            # check if the character is in s1 set
            substring = s2[l:r + len(s1)]
            if Counter(substring) == Counter(s1):
                return True

            l += 1

        return False
                

