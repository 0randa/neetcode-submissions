class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy_idx = 0
        sell_idx = 0
        profit = 0

        for i in range(1, len(prices)):
            curr_price = prices[i]
            buy_price = prices[buy_idx]
            sell_price = prices[sell_idx]

            # check if the current price is less than buy price
            if curr_price < buy_price:
                buy_idx = i
                sell_idx = i

            if prices[sell_idx] - prices[buy_idx] > profit:
                profit = prices[sell_idx] - prices[buy_idx]
            else:
                sell_idx = i



        return profit