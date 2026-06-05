class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        q = []

        for num in nums:
            heapq.heappush(q, (-num, num))


        for i in range(k-1):
            bruh = heapq.heappop(q)
            print(bruh)

        return heapq.heappop(q)[1]