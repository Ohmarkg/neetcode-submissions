class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minLeft = float('inf')
        maxProf = float('-inf')
        for num in prices:
            
            diff = num - minLeft
            maxProf = max(maxProf,diff)
            if num < minLeft :
                minLeft = num
        
        return max(0,maxProf)