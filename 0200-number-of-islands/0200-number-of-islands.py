class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        n = len(grid)
        m = len(grid[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= n or c >= m or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)                    
        
        return res
                                