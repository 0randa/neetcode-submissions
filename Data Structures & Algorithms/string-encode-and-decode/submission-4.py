class Solution:

    def encode(self, strs: List[str]) -> str:
        str_list = [x for x in strs]
        ret_string = " ".join(str_list)

        return ret_string

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]

        return s.split(" ")
