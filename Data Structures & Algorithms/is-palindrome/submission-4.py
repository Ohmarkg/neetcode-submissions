class Solution:
    #isalnum()

    def isPalindrome(self, s: str) -> bool:
       l,r = 0 , len(s) - 1
       while l < r:
        
        #move left until its at an alphanumeric char
        while l < r and not s[l].isalnum():
            l += 1
        
        while r > l and not s[r].isalnum():
            r -= 1
        #print(s[l] , s[r])
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
       return True


       
        