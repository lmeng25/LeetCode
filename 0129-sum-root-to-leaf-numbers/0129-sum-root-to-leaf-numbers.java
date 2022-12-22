/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int sumNumbers(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        res.add(0);
        dfs(root, res, 0);
        return res.get(0);
    }
    
    private void dfs(TreeNode node, List<Integer> res, int sum) {
        if (node == null)
            return;
        
        sum =  sum * 10 + node.val;
        
        if (node.left == null && node.right == null) {
            res.add(0, sum + res.get(0));
        }
        else {
            dfs(node.left, res, sum);
            dfs(node.right, res, sum);
        }
        
        sum -= node.val;
        sum /= 10;
    }
}