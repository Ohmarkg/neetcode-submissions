class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #"zxyzxyz"
        #"zxy"
        #"xy"

        current = set()
        maxcount = 0 
        i = 0
        for let in s:
            print(current , let)
            if let not in current:
                current.add(let)
                maxcount = max(len(current),maxcount)
            else:       
                
                while s[i] != let:
                    current.remove(s[i])
                    i += 1
                i += 1
        
        return maxcount       