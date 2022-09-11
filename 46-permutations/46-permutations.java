class Solution {
    List<List<Integer>> res = new LinkedList<>();
    
    public List<List<Integer>> permute(int[] nums) {
        List<Integer> dt = new LinkedList<>();
        List<Integer> perm = new LinkedList<>();
    
        for (int num : nums)
            dt.add(num);
        
        dfs(perm, dt);
        
        return res;
    }
    
    private void dfs(List<Integer> perm, List<Integer> dt) {
        if (dt.size() == 0) {
            res.add(perm);
            return;
        }
        
        for (int i = 0; i < dt.size(); i++) {
            List<Integer> tempDt = new LinkedList<>(dt);
            List<Integer> tempPerm = new LinkedList<>(perm);
            tempPerm.add(tempDt.get(i));
            tempDt.remove(tempDt.get(i));
            dfs(tempPerm, tempDt);
        }
    }
}