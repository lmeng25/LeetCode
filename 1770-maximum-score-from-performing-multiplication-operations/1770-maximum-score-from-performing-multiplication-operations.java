class Solution {
    public int maximumScore(int[] nums, int[] multipliers) {
        return dp(nums, multipliers, 0, 0, new int[nums.length][multipliers.length]);        
    }
    
    private int dp(int[] nums, int[] multipliers, int i, int left, int[][] memo) {
        if (i == multipliers.length)
            return 0;
        
        int right = nums.length - 1 - (i - left);
        
        if (memo[left][i] == 0) {
            memo[left][i] = Math.max(nums[left] * multipliers[i] + dp(nums, multipliers, i + 1, left + 1, memo), nums[right] * multipliers[i] + dp(nums, multipliers, i + 1, left, memo));                
        }
        
        return memo[left][i];
    }
}