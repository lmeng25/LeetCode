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
    public int kthSmallest(TreeNode root, int k) {
        PriorityQueue<Integer> q = new PriorityQueue();
        helper(root, q);
        for (int i = 0; i < k - 1; i++)
            q.poll();
        return q.peek();
    }
    
    private void helper(TreeNode root, PriorityQueue<Integer> q) {
        if (root != null) {
            helper(root.left, q);
            q.add(root.val);
            helper(root.right, q);
        }
    }
}