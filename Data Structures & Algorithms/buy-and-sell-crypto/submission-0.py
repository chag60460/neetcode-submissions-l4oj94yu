class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = 100
        max_profit = 0

        for price in prices:

            #each price could either be a potential sell price or a buy price
            
            #if it's smaller than min price, it's a buy price potentially
            #this means that for the prices after it, we are going to consider them as sell price
            #and evaluate the profit
            if price < min_price:
                min_price = price
            
            #if it subtracts current min price > max_profit, sell and update max_profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit