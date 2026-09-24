class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pairs = {}
        for i,num in enumerate(nums):
            pairs[num] = i
        
        for i,num in enumerate(nums):

            diff = target - num
            if (diff in pairs) and pairs[diff] != i:
                return [i,pairs[diff]]
        

        