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
    public boolean isValidBST(TreeNode root) {
        // if (root.left == null && root.right == null)
            // return true;
        return isBST(root.left, root.val, null) && isBST(root.right, null, root.val);
    }
    
    private boolean isBST(TreeNode node, Integer max, Integer min) {
        if (node == null)
            return true;
        
        if (max != null && node.val >= max)
            return false;
        
        if (min != null && node.val <= min)
            return false;
        
        return isBST(node.left, node.val, min) && isBST(node.right, max, node.val);
    }
}