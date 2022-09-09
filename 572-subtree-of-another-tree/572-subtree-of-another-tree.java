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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null)
            return false;
        
        return helper(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }
    
    private boolean helper(TreeNode root, TreeNode subRoot) {
        if (root == null)
            return subRoot == null;
        
        if (subRoot == null)
            return root == null;
        
        if (root.val != subRoot.val)
            return false;
        
        return helper(root.left, subRoot.left) && helper(root.right, subRoot.right);
    }
}