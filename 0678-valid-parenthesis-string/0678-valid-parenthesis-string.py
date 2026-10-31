class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = cmax = 0 

        for char in s:
            if char == "(":
                cmin += 1
                cmax += 1
            elif char == ")":
                cmin = max(cmin - 1, 0)
                cmax -= 1
            else:
                cmin = max(cmin - 1, 0) # if we use stare for opening
                cmax += 1 # if we use star for closing 
            
            if cmax < 0: # there are no stars left
                return False
        
        return cmin == 0

        