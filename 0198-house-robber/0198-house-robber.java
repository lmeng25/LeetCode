class Solution {
    private Map<Integer, Integer> map = new HashMap<>();
    private int[] nums;
    
    public int rob(int[] nums) {
        this.nums = nums;
        return dp(nums.length - 1);
    }
    
    private int dp(int i) {
        if (i == 0) return nums[0];
        if (i == 1) return Math.max(nums[0], nums[1]);
        if (!map.containsKey(i)) {
            map.put(i, Math.max(dp(i - 1), dp(i - 2) + nums[i]));
        }
        
        return map.get(i);
    }
}
