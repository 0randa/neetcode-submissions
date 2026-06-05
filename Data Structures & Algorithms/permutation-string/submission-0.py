class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_set = set(s1)

        s2_set = set()

        for char in s2:
            # check if the character is in s1 set
            if char in s1_set:
                # check if its already in s2 set
                if char in s2_set:
                    s2_set.clear()
                else:
                    s2_set.add(char)
            else:
                s2_set.clear()

            if s1_set == s2_set:
                return True


        return False
                

