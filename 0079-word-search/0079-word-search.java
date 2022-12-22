class Solution {
    private boolean found = false;
    
    public boolean exist(char[][] board, String word) {
    for (int row = 0; row < board.length; row++)
      for (int col = 0; col < board[0].length; col++) {
        dfs(row, col, word, board);
        if (found)
            return true;
      }
        return false;
    }
    
    private void dfs(int r, int c, String str, char[][] board) {
        char ch;
        if (str.equals("")) {
            found = true;
            return;            
        }
        
        if (r >= board.length || r < 0 || c < 0 || c >= board[0].length || board[r][c] != str.charAt(0))
            return;
        else {
            ch = board[r][c];
            board[r][c] = '0';
            dfs(r + 1, c, str.substring(1, str.length()), board);
            dfs(r - 1, c, str.substring(1, str.length()), board);
            dfs(r, c + 1, str.substring(1, str.length()), board);
            dfs(r, c - 1, str.substring(1, str.length()), board);
        }
        board[r][c] = ch;
    }
}