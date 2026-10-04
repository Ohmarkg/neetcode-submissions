class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numPos = {}
        
        for index, num in enumerate(nums):
            diff = target - num
            if diff in numPos:
                return [numPos[diff] , index]
            numPos[num] = index 
        