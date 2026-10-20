class Solution:

    def encode(self, strs: List[str]) -> str:
        # for each string, we can convert them to ascii
        # separate them by commas

        # then we can have underscores between the strings so we know where a string starts and ends
        # ["abc", "edf"]

        # "ascii(a),ascii(b),ascii(c)_ascii(e),ascii(d),ascii(f)"
        ret_str = ""
        for s in strs:
            if not s:
                ret_str += "_"
                continue

            for i in range(len(s) - 1):
                ret_str += f"{ord(s[i])},"
            ret_str += f"{ord(s[-1])}_"

        return ret_str
                

    def decode(self, s: str) -> List[str]:
        # "ascii(a),ascii(b),ascii(c)_ascii(e),ascii(d),ascii(f)"

        res = s.split("_")[:-1]
        ans = []
        for r in res:
            asciis = r.split(",")

            blob = "".join([chr(int(a)) for a in asciis if a])
            ans.append(blob)


        # ["ascii(a),ascii(b),ascii(c)", "ascii(e),ascii(d),ascii(f)"]
        # convert them back into characters

        return ans
