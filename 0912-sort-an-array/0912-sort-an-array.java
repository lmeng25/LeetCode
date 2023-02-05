class Solution {
    public int[] sortArray(int[] nums) {
        mergeSort(nums, 0, nums.length - 1);
        return nums;
    }
    
    private void mergeSort(int[] nums, int l, int r) {
        if (l >= r)
            return;
        
        int m = (l + r) / 2;
        mergeSort(nums, l, m);
        mergeSort(nums, m + 1, r);
        int[] leftHalf = Arrays.copyOfRange(nums, l, m + 1);
        int[] rightHalf = Arrays.copyOfRange(nums, m + 1, r + 1);
        
        int i = 0, j = 0, k = l;
        while (i < leftHalf.length && j < rightHalf.length) {
            if (leftHalf[i] < rightHalf[j])
                nums[k++] = leftHalf[i++];
            else
                nums[k++] = rightHalf[j++];
        }        
        
        while (i < leftHalf.length)
            nums[k++] = leftHalf[i++];
        while (j < rightHalf.length)
            nums[k++] = rightHalf[j++];
    }
}