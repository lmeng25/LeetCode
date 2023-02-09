class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            hset = set()
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] in hset:
                        return False
                    hset.add(board[i][j])
        
        for j in range(len(board[0])):
            hset = set()
            for i in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] in hset:
                        return False
                    hset.add(board[i][j])
        
        set_list = [set() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    idx = i // 3 + (j // 3) * 3
                    if board[i][j] in set_list[idx]:
                        return False
                    set_list[idx].add(board[i][j])
        
        
        return True