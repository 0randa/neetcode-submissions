class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        retList = []
        create_list = False
        for string in strs:
            if not retList:
                retList.append([string])
            else:
                for anagram in retList:
                    if sorted(anagram[0]) == sorted(string):
                        anagram.append(string)
                        create_list = False
                        break
                    create_list = True

                if create_list:
                    retList.append([string])

        return retList