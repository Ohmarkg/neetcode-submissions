class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = set()
        maxLength = 0
        startIndex = 0
        for let in s:
            while let in subString:
                subString.remove(s[startIndex])
                startIndex += 1
            subString.add(let)
            maxLength = max(maxLength,len(subString))
        return maxLength
