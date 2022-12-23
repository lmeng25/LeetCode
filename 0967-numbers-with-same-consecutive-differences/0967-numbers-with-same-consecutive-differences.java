class Solution {
    public int[] numsSameConsecDiff(int n, int k) {
        List<Integer> list = new ArrayList<>();
        
        for (int i = 1; i <= 9; i++) {
            dfs(i, n - 1, k, list, i);
        }
        
        int[] res = new int[list.size()];
        int i = 0;
        for (int num : list)
            res[i++] = num;
        
        return res;
    }
    
    private void dfs(int i, int n, int k, List<Integer> list, int num) {
        if (n == 0) {
            list.add(num);
            return;
        }
        
        for (int j = 0; j <= 9; j++) {
            if (j - i == k || i - j == k) {
                dfs(j, n - 1, k, list, num * 10 + j);
            }
        }
    }
}