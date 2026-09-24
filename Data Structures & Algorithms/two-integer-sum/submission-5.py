class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        count = {}

        #check the solution as we go

        for index,num in enumerate(nums):
            
            diff = target - num
            if diff in count and index != count[diff]:
                    return [count[diff],index] 
            elif diff not in count:
                count[num] = index
           

        