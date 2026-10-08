class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0
        
        bestBuy = prices[0]
        maxProfit  = 0
        i = 1
        while i < len(prices):
            bestBuy = min(bestBuy, prices[i])
            profit = prices[i] -bestBuy
            maxProfit = max(maxProfit,profit)
            i += 1
    
        return maxProfit
