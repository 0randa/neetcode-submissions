class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k

        pq = []

        for num in nums:
            heapq.heappush(pq, (num, num))

        self.pq = pq
        print(pq)

    def add(self, val: int) -> int:
            heapq.heappush(self.pq, (val, val))

            return self.pq[::-1][2][0]
        
