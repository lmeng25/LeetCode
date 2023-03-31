class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def rot(i, j, num):
            if i < 0 or j < 0 or i >= n or j >= m:
                return
            if grid[i][j] == 1:
                grid[i][j] = num + 1
            return
        
        haveOne = False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    haveOne = True
                    break
        if not haveOne:
            return 0
        
        start = 2
        stop = False
        while not stop:
            stop = True
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == start:
                        stop = False
                        rot(i - 1, j, start)
                        rot(i + 1, j, start)
                        rot(i, j - 1, start)
                        rot(i, j + 1, start)
            start += 1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        
        return start - 2 - 2
                        