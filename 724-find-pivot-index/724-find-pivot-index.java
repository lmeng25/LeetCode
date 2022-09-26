class Solution {
    public int pivotIndex(int[] nums) {
        int sum = 0;
        
        for(int num : nums)
            sum += num;
        
        int left = 0;
        int right;
        
        for (int i = 0; i < nums.length; i++) {
            if (i > 0)
                left += nums[i - 1];
            right = sum - left - nums[i];
            
            if (left == right)
                return i;
        }
        
        return -1;
    }
}