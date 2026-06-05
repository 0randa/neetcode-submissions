class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = ""

        length = len(word1)




        for i in range(length):

            if i >= len(word2):
                new_str += word1[i:]
                break

            new_str += word1[i]
            new_str += word2[i]

        if length < len(word2):
            new_str += word2[length:]


        return new_str



        
