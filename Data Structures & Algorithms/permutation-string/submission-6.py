class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        i, j = 0, len(s1)

        
        while j <= len(s2):
            
            cut = Counter(s2[i:j])

            if Counter(s1) == cut:
                return True

            i += 1
            j += 1

        return False
        