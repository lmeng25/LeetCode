class Solution {
    List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<Integer> list = new ArrayList<>();
        Arrays.sort(candidates);
        dfs(candidates, target, list, 0);
        return res;
    }
    
    private void dfs(int[] candidates, int target, List<Integer> list, int index) {
        if (target == 0) {
            res.add(new ArrayList<Integer>(list));
            return;
        }
        else if (target > 0) {
            for (int i = index; i < candidates.length; i++) {
                list.add(candidates[i]);
                dfs(candidates, target - candidates[i], list, i);
                list.remove(list.size() - 1);
            }
        }
        else {
            return;
        }
    }
}