class Solution {
    List<List<Integer>> res = new LinkedList<>();
    HashSet<List<Integer>> set = new HashSet<>();
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<Integer> dt = new LinkedList<>();
        List<Integer> permute = new LinkedList<>();
        
        for (int num : nums)
            dt.add(num);
        
        dfs(permute, dt);
        
        return res;
    }
    
    private void dfs(List<Integer> permute, List<Integer> dt) {
        if (dt.size() == 0) {
            if (!set.contains(permute)) {
                res.add(permute);
                set.add(permute);
            }
            return;
        }
        
        for (int i = 0; i < dt.size(); i++) {
            List<Integer> tempDt = new LinkedList<>(dt);
            List<Integer> tempPermute = new LinkedList<>(permute);
            tempPermute.add(tempDt.get(i));
            tempDt.remove(tempDt.get(i));
            dfs(tempPermute, tempDt);
        }
    }
}