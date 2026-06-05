class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        # have a left and right pointer


        max_profit = 0

        l, r = 0, 0

        # left pointer is buy price, right pointer is sell price.


        buy_price = 0

        min_buy = prices[0]

        for r, price in enumerate(prices):
            if prices[l] < price:
                max_profit = max(max_profit, price - prices[l])
                buy_price = price

            else:
                l = r



        return max_profit
