class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        int first = nums[0];
        
        if (nums.length == 1)
            return nums[0];
        
        if (nums[r] > nums[l])
            return nums[l];
        
        while (l <= r) {
            int mid = l + (r - l) / 2;
               
            if (nums[mid] > nums[mid + 1])
                return nums[mid + 1];
            
            if (nums[mid - 1] > nums[mid])
                return nums[mid];
            
            if (nums[mid] > first)
                l = mid + 1;
            else
                r = mid - 1;
        }
        
        return first;
    }
}