class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        foundNums = {}
        for n in nums:
            if n in foundNums:
                return True
            foundNums[n] =1 
        return False
        