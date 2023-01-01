class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1)
            return nums[0];
        
        int[] arr1 = new int[nums.length - 1];
        int[] arr2 = new int[nums.length - 1];
        
        for (int i = 0; i < nums.length - 1; i++)
            arr1[i] = nums[i];
        
        for (int i = 1; i < nums.length; i++)
            arr2[i - 1] = nums[i];
        
        return Math.max(dp(arr1, arr1.length - 1, new HashMap<Integer, Integer>()), dp(arr2, arr2.length - 1, new HashMap<Integer, Integer>()));
    }
    
    private int dp(int[] nums, int n, Map<Integer, Integer> memo) {
        if (n == 0)
            return nums[0];
        if (n == 1)
            return Math.max(nums[0], nums[1]);
        
        if (!memo.containsKey(n))
            memo.put(n, Math.max(dp(nums, n - 1, memo), dp(nums, n - 2, memo) + nums[n]));
        
        return memo.get(n);
    }
}