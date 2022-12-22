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
    int res = 0;
    public int sumNumbers(TreeNode root) {
        dfs(root, 0);
        return res;
    }
    
    private void dfs(TreeNode node, int sum) {
        if (node == null)
            return;
        
        sum = sum * 10 + node.val;
        
        if (node.left == null && node.right == null) {
            res += sum;
        }
        else {
            dfs(node.left, sum);
            dfs(node.right, sum);
        }
        
        sum -= node.val;
        sum /= 10;
    }
}