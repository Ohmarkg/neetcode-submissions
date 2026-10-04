class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums =  set(nums)
        found = set()
        maxStreak = 0
        for n in uniqueNums:
            if n in found:
                continue
            streak = 0
            current = n
            while current in uniqueNums:
                found.add(current)
                streak += 1
                maxStreak = max(streak, maxStreak)
                current += 1
            
        return maxStreak