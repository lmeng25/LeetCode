class Solution {
    public int deleteAndEarn(int[] nums) {
        int res = 0;
        int maxNum = 0;
        Map<Integer, Integer> points = new HashMap<>();
        
        // find max number, build hashmap
        for (int num : nums) {
            maxNum = Math.max(maxNum, num);
            points.put(num, points.getOrDefault(num, 0) + 1);
        }
    
        for (Map.Entry<Integer, Integer> set : points.entrySet())
            points.put(set.getKey(), set.getKey() * set.getValue());

        return maxPoint(maxNum, points, new HashMap<Integer, Integer>());
    }
    
    private int maxPoint(int num, Map<Integer, Integer> points, Map<Integer, Integer> memo) {
        if (num == 0)
            return 0;
        if (num == 1)
            return points.getOrDefault(1, 0);
        
        if (memo.containsKey(num))
            return memo.get(num);
        
        int res = Math.max(maxPoint(num - 1, points, memo), maxPoint(num - 2, points, memo) + points.getOrDefault(num, 0));
        
        memo.put(num, res);
        return res;
    }
}