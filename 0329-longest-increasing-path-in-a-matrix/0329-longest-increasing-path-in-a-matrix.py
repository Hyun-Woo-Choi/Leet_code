class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:

        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])

        memo = {}
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r: int, c:int) -> int:
            if (r, c) in memo:
                return memo[(r, c)]
            
            max_len = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))
                
            memo[(r, c)] = max_len
            return max_len
        
        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r,c))
    
        return ans