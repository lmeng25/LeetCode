class Solution {
    public int[] getModifiedArray(int length, int[][] updates) {
        int[] res = new int[length];
        
        for (int[] arr : updates) {
            for (int i = arr[0]; i <= arr[1]; i++)
                res[i] += arr[2];        
        }
        
        return res;
    }
}