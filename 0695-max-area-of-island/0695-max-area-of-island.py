class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        m = len(grid[0])
        
        def dfs(i, j, area):
            nonlocal res
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] != 1:
                return area
            grid[i][j] = 0
            area += 1
            area = dfs(i + 1, j, area)
            area = dfs(i - 1, j, area)
            area = dfs(i, j + 1, area)
            area = dfs(i, j - 1, area)
            res = max(res, area)
            return area
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(i, j, 0)
        
        return res