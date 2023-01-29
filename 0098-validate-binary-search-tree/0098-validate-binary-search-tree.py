# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBst(root, high, low):
            if root == None:
                return True
            if low != None and root.val <= low:
                return False
            if high != None and root.val >= high:
                return False
            return isBst(root.left, root.val, low) and isBst(root.right, high, root.val)
        
        return isBst(root, None, None)