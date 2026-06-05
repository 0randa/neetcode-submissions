class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # We get the current amount, then subtract it by the largest number that is smaller than it
        coins.sort()

        # while amount > 0:
        change = 0
        while amount > 0:
            subtracted = False
            for coin in coins[::-1]:
                print("hi")
                if coin <= amount:
                    print("ok")
                    amount -= coin
                    change += 1
                    subtracted = True
                    break
            if not subtracted:
                return -1

        return change