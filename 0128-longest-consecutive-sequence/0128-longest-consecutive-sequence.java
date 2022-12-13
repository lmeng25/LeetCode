class Solution {
    public int longestConsecutive(int[] nums) {
        // construct min heap
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int num : nums)
            heap.add(num);
        
        int len, res = 0;
        while (!heap.isEmpty()) {
            int left = heap.poll();
            len = 1;
            while (!heap.isEmpty() && heap.peek() - left <= 1) {
                if (heap.peek() - left == 1)
                    len++;
                left = heap.poll();
            }
            res = Math.max(res, len);
        }
        
        return res;
    }
}