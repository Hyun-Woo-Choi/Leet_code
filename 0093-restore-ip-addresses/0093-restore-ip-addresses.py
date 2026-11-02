"""
    Problem:
        given a string, divide it to valid ip addresses
    
    Q1. can we exclude some part of string? 
    -> No, longest length of string can be 12
    3 * 4 = 12

    Intutition:
        from the string, move the dots from the first to last, and if its valid 
        add it to output
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        
        res = []

        def backtrack(start_idx: int, path: list[str]):
            if len(path) == 4:
                if start_idx == len(s):
                    res.append(".".join(path))
                return 
            
            for length in range(1,4):
                if start_idx + length > len(s):
                    break
                
                segment = s[start_idx: start_idx + length]

                if len(segment) > 1 and segment[0] == "0":
                    break
                
                if int(segment) > 255:
                    break
                
                path.append(segment)
                backtrack(start_idx + length, path)
                path.pop()
        backtrack(0, [])
        return res

        