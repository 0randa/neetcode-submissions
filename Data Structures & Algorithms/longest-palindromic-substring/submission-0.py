class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        def getOddPalins():
            res, resLen = s[0], 1
            for i, c in enumerate(s):
                l, r = i - 1, i + 1

                while (l >= 0 and r < len(s)):
                    if s[l] != s[r]:
                        palin = s[l + 1:r] 
                        if len(palin) > resLen:
                            res = palin
                            resLen = len(palin)
                        break

                    l -= 1
                    r += 1
                else:            
                    palin = s[l + 1:r] 
                    if len(palin) > resLen:
                        res = palin
                        resLen = len(palin)

            return res


        def getEvenPalins():
            res, resLen = s[0], 1
            for i, c in enumerate(s):
                l, r = i - 1, i + 2
                

                if i + 1 < len(s) and c == s[i + 1]:

                    while (l >= 0 and r < len(s)):
                        if s[l] != s[r]:
                            palin = s[l + 1:r] 
                            if len(palin) > resLen:
                                res = palin
                                resLen = len(palin)
                            break

                        l -= 1
                        r += 1
                    else:            
                        palin = s[l + 1:r] 
                        if len(palin) > resLen:
                            res = palin
                            resLen = len(palin)
                
            return res


        odd = getOddPalins()

        if len(getOddPalins()) > len(getEvenPalins()):
            return getOddPalins()

        return getEvenPalins()

                
                    



