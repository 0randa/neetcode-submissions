class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = sorted(list(s))
        arr2 = sorted(list(t))

        return arr1 == arr2