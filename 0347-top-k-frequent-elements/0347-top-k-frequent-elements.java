class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        
        PriorityQueue<Map.Entry<Integer, Integer>> queue = new PriorityQueue<>(Map.Entry.comparingByValue(Comparator.reverseOrder()));
        
        for (Map.Entry<Integer, Integer> set : map.entrySet()) {
            queue.add(set);
        }
        
        int[] res = new int[k];
        
        for (int i = 0; i < k; i++) {
            res[i] = queue.poll().getKey();
        }
        
        return res;
    }
}