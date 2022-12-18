class Solution {
    public int search(int[] nums, int target) {
        
        int l = 0;
        int r = nums.length - 1;
        int mid;
        int pivot = 0;
        
        if (nums[0] == target)
            return 0;
        
        if (nums.length == 1)
            return nums[0] == target ? 0 : -1;

        if (nums[0] < nums[nums.length - 1])
            pivot = 0;
        else {
            while (l <= r) {
                pivot = l + (r - l) / 2;

                if (nums[pivot + 1] < nums[pivot]) {
                    pivot++;
                    break;
                }

                if (nums[l] > nums[pivot])
                    r = pivot;
                else
                    l = pivot;
            }    
        }

        if (pivot != 0) {
            if (nums[0] < target) {
                l = 0;
                r = pivot;
            }
            else {
                l = pivot;
                r = nums.length - 1;
            }
        }
        else {
            l = 0;
            r = nums.length - 1;
        }
            
        while (l <= r) {
            mid = l + (r - l) / 2;
            
            if (nums[mid] == target)
                return mid;
            
            if (nums[mid] < target){
                l = mid + 1;
            }
            else {
                r = mid - 1;
            }
        }
        
        return -1;
    }
}