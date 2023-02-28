class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        n = len(heights)
        m = len(heights[0])
        
        def dfs(i, j, visited, lastHeight):
            if (i, j) in visited:
                return
            if i < 0 or j < 0 or i > n - 1 or j > m - 1:
                return
            if heights[i][j] < lastHeight:
                return
            visited.add((i, j))
            dfs(i + 1, j, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])
        
        for i in range(n):
            dfs(i, 0, pac, 0)
            dfs(i, m - 1, atl, 0)
        
        for j in range(m):
            dfs(0, j, pac, 0)
            dfs(n - 1, j, atl, 0)
            
        res = []
        for item in pac:
            if item in atl:
                res.append(item)
                
        return res