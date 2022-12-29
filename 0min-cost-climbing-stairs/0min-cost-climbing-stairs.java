class Solution {
    Map<Integer, Integer> map = new HashMap<>();
    public int minCostClimbingStairs(int[] cost) {
        return helper(cost.length, cost);
    }
    
    private int helper(int i, int[] cost) {
        if (i == 0 || i == 1)
            return 0;
        
        if (!map.containsKey(i))
            map.put(i, Math.min(helper(i - 1, cost) + cost[i - 1], helper(i - 2, cost) + cost[i - 2]));
        
        return map.get(i);
    }
}