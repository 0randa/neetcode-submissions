class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        blob = set()

        def recur(sublist):
            if not sublist:
                return -1
            
            if sublist[0] in blob:
                return sublist[0]
            else:
                blob.add(sublist[0])

            return recur(sublist[1:])

        return recur(nums)