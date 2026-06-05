class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        _dict = {}

        for s in strs:
            sorted_string = "".join(sorted(s))

            if sorted_string not in _dict:
                _dict[sorted_string] = [s]
            else:
                _dict[sorted_string].append(s)


        return [i for i in _dict.values()]