class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Must same length
        if len(s) != len(t):
            return False
        
        counts = [0] * (ord('z') - ord('a') + 1)

        
        for i in range(len(s)):
            counts[ord(s[i]) % ord('a')] += 1
            counts[ord(t[i]) % ord('a')] -= 1
        
        for freq in counts:
            if freq != 0:
                return False
        return True
            