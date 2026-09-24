class Solution:
    def isPalindrome(self, s: str) -> bool:
       l = 0
       r = len(s) - 1

       # loop until l <= right 
       # move left and right to an alpha nurmeric character
       # compare 
       # increment both pointers by one
       s = s.lower()
       while l <= r:

            #move left
            while l < r and not(s[l].isalnum()) :
                l += 1
            
            #move right
            while r >l and not(s[r].isalnum()):
                r -= 1
            print(l,r)
            if s[l] != s[r]:
                print(s[l],s[r])
                return False
            l += 1
            r -= 1
       return True
            
        