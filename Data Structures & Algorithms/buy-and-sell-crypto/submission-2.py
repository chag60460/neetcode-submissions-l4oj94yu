class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Keep track of the maximum profit
        max_profit = 0

        # Keep track of the minimum price
        min_price = 100

        for price in prices:

            # Consider this as either buy price
            if price < min_price:
                min_price = price
            
            # Or Consider this as sell price
            elif ((price - min_price) > max_profit):
                max_profit = price - min_price
        
        return max_profit
