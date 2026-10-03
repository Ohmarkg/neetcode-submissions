class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Must same length
        if len(s) != len(t):
            return False
        
        Scount  = {}
        Tcount  = {}

        for let in s:
            Scount[let] = Scount.get(let,0) + 1
        for let in t:
            Tcount[let] = Tcount.get(let,0) + 1
        
        for let in Scount:
            if let not in t or Scount[let] != Tcount[let]:
                return False
        return True