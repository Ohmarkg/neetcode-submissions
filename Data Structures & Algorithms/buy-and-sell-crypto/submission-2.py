class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #track the best buying price so far 
        #compare with the sell price is  and adjust

        bestBuy = prices[0]
        profit = 0
        for n in prices:
            
            bestBuy = min(bestBuy, n)
            profit = max(profit, n - bestBuy)
        return profit
        