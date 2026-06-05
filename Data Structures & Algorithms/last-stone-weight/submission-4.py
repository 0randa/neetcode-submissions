class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []

        for stone in stones:
            heapq.heappush(q, (-stone, stone))



        while len(q) > 1:
            (rock1Pri, rock1Val), (rock2Pri, rock2Val) = heapq.heappop(q), heapq.heappop(q)

            difference = rock1Val - rock2Val

            if difference > 0:
                heapq.heappush(q, (-difference, difference))

                
        if not q:
            return 0

        return q[0][1]