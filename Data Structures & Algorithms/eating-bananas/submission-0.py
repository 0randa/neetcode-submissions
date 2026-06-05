class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # Lower and upper bounds for k
        result = r  # Store the minimum valid k

        while l <= r:
            middle = (l + r) // 2  # Midpoint of the current range

            # Calculate total time to eat all bananas at speed `middle`
            eatingTime = self.timeToEatBananas(piles, middle)

            if eatingTime <= h:  # If possible to finish within h hours
                result = middle  # Update result with the current speed
                r = middle - 1  # Try for a smaller speed
            else:  # If not possible, increase speed
                l = middle + 1

        return result

    def timeToEatBananas(self, piles: List[int], speed: int) -> int:
        retVal = 0
        for bananas in piles:
            retVal += math.ceil(bananas / speed)  # Calculate time for each pile
        return retVal