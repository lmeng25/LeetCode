class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        int mid;
        
        if (nums.length == 1)
            return nums[0];
        
        while (l <= r) {
            mid = (l + r) / 2;
            
            if (mid == 0)
                return nums[mid] > nums[mid + 1] ? nums[mid + 1] : nums[mid];
            
            if (nums[mid] < nums[mid - 1])
                return nums[mid];
            
            if (nums[mid] >= nums[l] && nums[mid] > nums[r])
                l = mid + 1;
            else
                r = mid - 1;
        }
        
        return nums[r];
    }
}