class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        _min, profit = prices[0], 0
        for price in prices[1:]:

            # so we can either buy or sell

            if price < _min:
                _min = price
            elif price > _min:
                profit = max(profit, price - _min)
        
        return profit


