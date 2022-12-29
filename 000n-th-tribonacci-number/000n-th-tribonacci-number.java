class Solution {
    Map<Integer, Integer> memo = new HashMap<>();
    public int tribonacci(int n) {
        return trib(n);
    }
    
    private int trib(int n) {
        memo.put(0, 0);
        memo.put(1, 1);
        memo.put(2, 1);
        
        if (!memo.containsKey(n))
            memo.put(n, trib(n - 1) + trib(n - 2) + trib(n - 3));
        return memo.get(n);
    }
}