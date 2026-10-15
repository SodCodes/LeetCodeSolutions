class Solution:
    """
    Plan: Store the 1st number, iteriate through each num if num is less than mini store it as new mini if not subtract from minimum number and take the bigger number between that total or existing value of profit.
    Time: O(n) , n = integers in prices, we look at each number once in 1 pass of prices
    Space: O(1), the constant is 0 to n 
    """


    def maxProfit(self, prices: list[int]) -> int:
        
        profit = 0
        
        #edge case if length of prices is 1, there's not a day to sell
        if len(prices) == 1:
            return profit
            
        #day to buy, set it as 1st number 
        minimum = prices[0]
        
        for num in prices[1:]:
            
            if num > minimum:
                profit = max(profit, num - minimum)
            else:
                minimum = num
        
        return profit    

  
    
    

"""
1st Solution:
class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        
        #edge case if len of prices is 1
        if len(prices) == 1:
            return 0
        
        #store the max and min number
        maximum = 0
        minimum = 0
        
        #profit
        profit = 0
        
        #default day ot sell as 0
        sell_day = 0
        
        for day, num in enumerate(prices):
            
            if minimum == 0 or num < minimum:
                minimum = num
                buy_day = day
                
            
            if num > maximum:
                if day > buy_day:
                    maximum = num
                    sell_day = day
                    profit = maximum - minimum
               
            
            return the highest profit possible
            #reset profit and maxiumum        
            if buy_day > sell_day:
                profit = 0 
                maximum = 0

            
        return profit   

"""