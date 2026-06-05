class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) 
        result = r  

        while l <= r:
            middle = (l + r) // 2 

            eatingTime = self.timeToEatBananas(piles, middle)

            if eatingTime <= h:
                result = middle
                r = middle - 1 
            else:  
                l = middle + 1

        return result

    def timeToEatBananas(self, piles: List[int], speed: int) -> int:
        retVal = 0
        for bananas in piles:
            retVal += math.ceil(bananas / speed) 
        return retVal