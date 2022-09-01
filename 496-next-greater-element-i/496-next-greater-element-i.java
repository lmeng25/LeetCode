class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] res = new int[nums1.length];
        
        // create a hashmap to store the num and next greater element respectively 
        HashMap<Integer, Integer> map = new HashMap<>();
        
        // loop through nums2 
        for (int i = 0; i < nums2.length; i++) {
            int nextGreater;
            
            // find and put num-nextGreater into hashmap
            for (int j = i + 1; j < nums2.length; j++) {
                if (nums2[j] > nums2[i]) {
                    map.put(nums2[i], nums2[j]);
                    break;
                }
            }
            if (!map.containsKey(nums2[i]))
                map.put(nums2[i], -1);
        }
        
        
        for (int i = 0; i < nums1.length; i++) {
            res[i] = map.get(nums1[i]);
        }
        
        return res;
    }
}