from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def dfs(i, j):
            # Vase case: if we reached the end of pattern.
            # we must also be at the end of the string
            if j == len(p):
                return i == len(s)

            # Check if the current characters match
            current_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j + 1 < len(p) and p[j+1] == '*':
                return dfs(i, j + 2) or (current_match and dfs(i + 1, j))
            
            if current_match:
                return dfs(i + 1, j + 1)
            
            return False

        return dfs(0, 0)
