class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []

        for num in nums:
            res.append([-num, num])

        heapq.heapify(res)

        while k > 1:
            priority, elt = heapq.heappop(res)

            k -= 1

        return heapq.heappop(res)[1]