class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] res = new int[cost.length + 1];

        for (int i = 2; i < cost.length + 1 ; i++) {
            res[i] = Math.min(res[i - 1] + cost[i - 1], res[i - 2] + cost[i - 2]);
        }
        
        return res[cost.length];
    }
}