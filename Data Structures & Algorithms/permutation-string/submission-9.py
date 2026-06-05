class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        array1 = [0] * 26
        array2 = [0] * 26

        if s1 == s2:
            return True

        if len(s2) < len(s1):
            return False

        def get_index_from_ascii(c):
            return ord(c) - 97

        for c in s1:
            index = get_index_from_ascii(c)
            array1[index] += 1
    
        for i in range(len(s1)):
            first_char = get_index_from_ascii(s2[i])
            array2[first_char] += 1

        l, r = 0, len(s1)

        if array1 == array2:
            return True

        while r < len(s2):
            first_char = get_index_from_ascii(s2[l])
            last_char = get_index_from_ascii(s2[r])

            # first character should be removed
            array2[first_char] -= 1

            # most recent character should be added
            array2[last_char] += 1

            l += 1
            r += 1

            if array1 == array2:
                return True

        return False

