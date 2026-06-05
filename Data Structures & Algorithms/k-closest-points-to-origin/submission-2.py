class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []
        heapq.heapify(res)

        def euclid(x1,y1):
            x2, y2 = 0, 0
            return math.sqrt((x1-x2)**2 + (y1-y2)**2)

        for index, coord in enumerate(points):
            x, y = coord
            distance = euclid(x,y)
            heapq.heappush(res,(distance,index))

        

        sol = []

        while res:
            if len(sol) == k:
                break
            elt, index = heapq.heappop(res)
            sol.append(points[index])
        
        return sol