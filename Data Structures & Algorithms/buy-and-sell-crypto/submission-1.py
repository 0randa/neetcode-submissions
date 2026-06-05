class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use a sliding window to keep track of the min

        sell_price = 0
        buy_price = prices[0]

        profit = 0
        for i in range(1, len(prices) - 1):
            curr_price = prices[i]
            if curr_price < buy_price:

                # get the index of the max element, and find the different

                largest_future = max(prices[i:])

                if largest_future - curr_price > profit:
                    profit = largest_future - curr_price


        return profit

        