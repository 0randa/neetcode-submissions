class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)

        dp[0] = True

        for i in range(len(s) + 1):

            for word in wordDict:
                # word has to be less than current length of the string
                if len(word) <= i:
                    # check if the last length of the word characters are the same as the length of the word
                    if s[i-len(word):i] == word and dp[i-len(word)] == True:
                        dp[i] = True

        return dp[-1]


