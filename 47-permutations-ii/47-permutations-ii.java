class Solution {
    List<List<Integer>> res = new LinkedList<>();
    public List<List<Integer>> permuteUnique(int[] nums) {
        Map<Integer, Integer> dt = new HashMap<>();
        List<Integer> permute = new LinkedList<>();
        
        for (int num : nums)
            dt.put(num, dt.getOrDefault(num, 0) + 1);
        
        dfs(permute, dt);
        
        return res;
    }
    
    private void dfs(List<Integer> permute, Map<Integer, Integer> dt) {
        if (dt.isEmpty()) {
            res.add(permute);
            return;
        }
        
        for (int num : dt.keySet()) {
            Map<Integer, Integer> tempDt = new HashMap<>(dt);
            List<Integer> tempPermute = new LinkedList<>(permute);
            tempPermute.add(num);
            tempDt.put(num, tempDt.get(num) - 1);
            if (tempDt.get(num) == 0)
                tempDt.remove(num);
            dfs(tempPermute, tempDt);
        }
    }
}