class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #idea is to track the max left and right height values
        # move the side the has the less height 
        # continue until l and r reach other
        l,r = 0 , len(heights) - 1
        maxWater = -1

        while l < r:
            
            width = r - l
            height = min(heights[l] , heights[r])
            water = width * height
    
            #shift the the lower height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1


            #recalc
            maxWater = max(maxWater, water)
        return maxWater

        