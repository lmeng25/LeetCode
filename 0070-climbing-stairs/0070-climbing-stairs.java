class Solution {
    public int climbStairs(int n) {
        return helper(n, new HashMap<Integer, Integer>());
    }
    
    private int helper(int n, Map<Integer, Integer> map) {
        if (n == 0)
            return 0;
        if (n == 1 || n == 2)
            return n;
        
        if (!map.containsKey(n)) {
            map.put(n, helper(n - 1, map) + helper(n - 2, map));
        }
        
        return map.get(n);
    }
}