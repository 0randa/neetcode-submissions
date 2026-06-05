class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        used_chance = False


        l,r = 0, len(s) - 1


        while l < r:


            if s[l] != s[r]:
                # check for used chance

                if used_chance:
                    return False
                
                # 
                if s[l + 1] == s[r]:
                    l += 1

                elif s[l] == s[r - 1]:
                    r -= 1
                else:
                    return False
                used_chance = True
                # 
            else: 
                l += 1
                r -= 1
        return True
