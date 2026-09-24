class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        let1 = {}
        let2 = {}
        for let in s:
            if let in let1:
                let1[let] += 1
            else:
                let1[let] = 1
        for let in t:
            if not let in let1:
                return False

            if let in let2:
                let2[let] += 1
            else:
                let2[let] = 1

        for key in let1:
            if  not(key in let2 and let1[key] == let2[key]):
                return False
        return True