class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums =  set(nums)
        maxStreak = 0
        for n in uniqueNums:
            if  (n - 1) in uniqueNums:
                continue
            streak = 0
            current = n
            while current in uniqueNums:
                streak += 1
                current += 1
            maxStreak = max(streak, maxStreak)
        return maxStreak