class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        
        def dfs(i, j):
            if i < 0 or j < 0 or i > n - 1 or j > m - 1:
                return
            if board[i][j] == "O":
                board[i][j] = "T"
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)
                return
        
        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        
        for j in range(m):
            dfs(0, j)
            dfs(n - 1, j)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"
