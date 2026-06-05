class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        blob = set()

        def recur(sublist):
            if not sublist:
                return -1
            
            cur = sublist[0]

            if cur in blob:
                return cur
            else:
                blob.add(cur)

            return recur(sublist[1:])

        return recur(nums)