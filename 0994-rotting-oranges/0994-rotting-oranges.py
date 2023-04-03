class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        rotten = deque()
        time = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    rotten.append([i, j])
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while rotten and fresh:
            for k in range(len(rotten)):
                i, j = rotten.popleft()
                for dr, dc in directions:
                    ni = i + dr
                    nj = j + dc
                    if ni >= 0 and nj >= 0 and ni < n and nj < m and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        rotten.append([ni, nj])
            time += 1
        
        return time if fresh == 0 else -1