# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        
        def dfs(root, currMax):
            if not root:
                return 
            nonlocal res
            dfs(root.left, max(root.val, currMax))
            if root.val >= currMax:
                res += 1
            dfs(root.right, max(root.val, currMax))
        
        dfs(root, root.val)
        return res
            
        