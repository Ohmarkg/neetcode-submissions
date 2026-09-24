class Solution:
    def isValid(self, s: str) -> bool:
        matchP = {"}":"{" , "]":"[" , ")":"("}
        closeP = {"}", "]" , ")"}
   
        if len(s) % 2 == 1:
            return False
        
        lets = list(s)
        buff = []
        while len(lets) > 0:
            temp = lets.pop(0)

            if temp in closeP:
                if not buff:
                    return False
                elif matchP[temp] != buff[-1]:
                    return False
                else:
                    buff.pop(-1)
            else:
                buff.append(temp)
        return len(buff) == 0


            


            
                
        