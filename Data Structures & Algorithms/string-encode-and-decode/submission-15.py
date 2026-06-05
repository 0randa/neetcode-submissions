class Solution:
    separator = "grasdasd#!@$@$"

    def encode(self, strs: List[str]) -> str:
        # encode into a string, separate it all by spaces
        if not strs:
            return "EMPTY"


        ret_string = Solution.separator.join(strs)

        return ret_string


    def decode(self, s: str) -> List[str]:
        if s == "EMPTY":
            return []

        decode_array = s.split(Solution.separator)

        return decode_array