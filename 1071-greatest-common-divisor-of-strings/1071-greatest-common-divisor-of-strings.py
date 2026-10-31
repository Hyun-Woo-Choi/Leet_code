"""
    problem: given two arrays, needtto find the greatest common divisor of strings. 


"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def divides(base: str, target:str) -> bool:
            if len(target) % len(base) != 0:
                return False
            
            repeat_factor = len(target) // len(base)
            return base * repeat_factor == target
        
        for length in range(min(len1, len2), 0, -1):
            if len1 % length == 0 and len2 % length == 0:
                candidate = str1[:length]
                if divides(candidate, str1) and divides(candidate, str2):
                    return candidate
        
        return ""