class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_set = set(s1)

        s2_str = ""

        for char in s2:
            # check if the character is in s1 set
            if char in s1_set:
                s2_str += (char)
            else:
                s2_str = ""

            if Counter(s1) == Counter(s2_str):
                return True


        return False
                

