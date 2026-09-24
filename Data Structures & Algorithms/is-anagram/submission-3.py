class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #if the lens are not the same 

        if len(s) != len(t):
            return False


        #convert to dictionaries
        c1 = {}
        c2 = {}

        for num in s:

            if num in c1:
                c1[num] += 1
            else:
                c1[num] = 1

        for num in t:

            if num in c2:
                c2[num] += 1
            else:
                c2[num] = 1

        for num in c1:
            if num not in c2 or c1[num] != c2[num]:
                return False
    
        return True
        
      