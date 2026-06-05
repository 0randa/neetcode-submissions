class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_str = ''.join(char for char in s if char.isalnum())

        for i in range(int(len(alnum_str) / 2)):
            j = len(alnum_str) - i - 1
            
            if alnum_str[i].casefold() != alnum_str[j].casefold():
                return False

        return True