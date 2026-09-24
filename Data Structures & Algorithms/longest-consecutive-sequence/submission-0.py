class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        uniquenums = set(nums)
        seen = set()
        maxseq = 0
        for num in uniquenums:
            curr = num
            count = 1
            if num in seen:
                continue
            while curr + 1 in uniquenums:
                seen.add(curr)
                count +=1
                curr +=1
            maxseq = max(maxseq,count)
        return maxseq
                
        
        
        