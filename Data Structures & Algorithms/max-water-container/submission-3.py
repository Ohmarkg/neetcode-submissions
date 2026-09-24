class Solution:
    def maxArea(self, heights: List[int]) -> int:
            left = 0
            right = len(heights) -1
            #find the first left
            while heights[left] == 0:
                left += 1
            
            #find the first right
            while heights[right] == 0:
                right -= 1

            
            maxarea = 0
            maxbound = [left,right]
            while left != right:

                #calculate the potential area 
                area = min(heights[left],heights[right]) * (right - left)

                if area > maxarea:
                    maxarea = area
                    #reset our max bound
                    maxbound[0] = left
                    maxbound[1] = right
                elif heights[left] <= heights[right]:
                    left +=1 
                elif heights[right] < heights[left]:
                    right -= 1
                
            print(maxbound)
            return maxarea
        