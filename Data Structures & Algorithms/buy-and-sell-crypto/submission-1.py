class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = 100
        max_profit = 0

        for price in prices:
            #Each price can either be a buy price
            if price < min_price:
                min_price = price
            #Or a sell price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit