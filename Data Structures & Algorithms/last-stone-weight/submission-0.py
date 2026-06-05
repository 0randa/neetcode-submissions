class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        pq = []

        if len(stones) == 2:
            return abs(list[0] - list[1])


        for stone in stones:
            heapq.heappush(pq, (-stone, stone))


        listi = []

        while pq:
            if len(listi) == 2:
                print(listi)
                difference = abs(listi[0] - listi[1])
                if difference > 0:
                    heapq.heappush(pq, (-difference, difference))
                listi = []

            priority, value = heapq.heappop(pq)
            listi.append(value)

        return listi[0]