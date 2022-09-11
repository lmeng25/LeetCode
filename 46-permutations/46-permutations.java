class Solution {
    List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> permute(int[] nums) {
        List<Integer> dt = new ArrayList<>();
        List<Integer> permutation = new ArrayList<>();
        for (int num : nums)
            dt.add(num);
        
        dfs (permutation, dt);
        
        return res;
    }
    
    private void dfs(List<Integer> permutation, List<Integer> dt) {
        if (dt.size() == 0) {
            res.add(permutation);
            return;
        }
        
        for (int i = 0; i < dt.size(); i++) {
            List<Integer> tempP = new ArrayList<>(permutation);
            List<Integer> tempDt = new ArrayList<>(dt);
            tempP.add(dt.get(i));
            tempDt.remove(dt.get(i));
            dfs(tempP, tempDt);
        }
    }
}