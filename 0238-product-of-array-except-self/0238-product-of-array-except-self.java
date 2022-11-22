class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] toLeft = new int[nums.length];
        int[] toRight = new int[nums.length];
        int[] res = new int[nums.length];
        
        int product = 1;
        toLeft[0] = 1;
        toRight[nums.length - 1] = 1;
        
        for (int i = 1; i < nums.length; i++) {
            toLeft[i] = product * nums[i - 1];
            product *= nums[i - 1];
        }
        
        product = 1;
        
        for (int i = nums.length - 2; i >= 0; i--) {
            toRight[i] = product * nums[i+ 1];
            product *= nums[i + 1];
        }
        
        for (int i = 0; i < nums.length; i++) {
            res[i] = toLeft[i] * toRight[i];
        }
        
        return res;
    }
}