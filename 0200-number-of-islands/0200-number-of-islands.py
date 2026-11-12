class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        R = len(grid)
        C = len(grid[0])
        answer = 0

        def dfs(r,c):
            if not (0 <= r < R and 0 <= c <C) or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                dfs(r + dr, c + dc)

        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1":
                    dfs(i,j)
                    answer += 1
        return answer
        