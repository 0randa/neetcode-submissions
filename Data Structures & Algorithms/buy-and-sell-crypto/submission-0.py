class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use a sliding window to keep track of the min

        sell_price = 0
        buy_price = prices[0]

        buy_index = 0
        for i in range(1, len(prices) - 1):

            if prices[i] < buy_price:
                buy_price = prices[i]
                buy_index = i
            
        print("buy price,", buy_price)
        print(f"buy index, {buy_index}")

        sell_price = max(prices[buy_index:])

        print(sell_price)

        return sell_price - buy_price

        