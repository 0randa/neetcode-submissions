class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # constant space, so we create an array of size 26
        if len(s) != len(t):
            return False

        arr = [0] * 26

        for letter in s:
            _ascii = ord(letter) - 97
            arr[_ascii] += 1

        for letter in t:
            _ascii = ord(letter) - 97
            arr[_ascii] -= 1


        return arr == [0] * 26