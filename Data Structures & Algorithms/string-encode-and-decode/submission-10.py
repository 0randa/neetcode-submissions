class Solution:
    EMPTY_ARRAY = False
    def encode(self, strs: List[str]) -> str:
        if not strs:
            Solution.EMPTY_ARRAY = True

        ret_string = " ".join(strs)

        return ret_string

    def decode(self, s: str) -> List[str]:
        print(s)
        print(s.split(" "))
        if Solution.EMPTY_ARRAY:
            return []
        return s.split(" ")
