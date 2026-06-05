class Solution:
    separator = "grasdasd#!@$@$"

    def encode(self, strs: List[str]) -> str:
        # encode into a string, separate it all by spaces

        ret_string = Solution.separator.join(strs)
        print(ret_string)

        return ret_string


    def decode(self, s: str) -> List[str]:
        decode_array = s.split(Solution.separator)

        return decode_array