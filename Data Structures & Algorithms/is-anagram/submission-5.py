class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Must same length
        if len(s) != len(t):
            return False
        
        sCount = [0] * (ord('z') - ord('a') + 1)
        tCount = [0] * (ord('z') - ord('a') + 1)
        
        for let in s:
            sCount[ord(let)%ord('a')] += 1
        for let in t:
            tCount[ord(let)%ord('a')] += 1
        
        for i in range(len(sCount)):
            if sCount[i] != tCount[i]:
                return False
        return True
            