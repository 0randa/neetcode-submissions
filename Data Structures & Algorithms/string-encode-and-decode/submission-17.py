class Solution:
    separator = "grasdasd#!@$@$"
    EMPTY_ARRAY = "EMPTY"
    def encode(self, strs: List[str]) -> str:
        # encode into a string, separate it all by spaces
        if not strs:
            return Solution.EMPTY_ARRAY

        ret_string = Solution.separator.join(strs)
        return ret_string


    def decode(self, s: str) -> List[str]:
        if s == Solution.EMPTY_ARRAY:
            return []

        decode_array = s.split(Solution.separator)
        return decode_array