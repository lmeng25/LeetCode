class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] res = new int[nums1.length];
        
        Stack<Integer> stack = new Stack<>();
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums2.length; i++) {
            int n = nums2[i];
            
            while (!stack.empty() && stack.peek() < n)
                map.put(stack.pop(), n);
            
            stack.push(n);
        }
        
        while (!stack.empty())
            map.put(stack.pop(), -1);
        
        for (int i = 0; i < nums1.length; i++) {
            res[i] = map.get(nums1[i]);
        }
        
        return res;
    }
}