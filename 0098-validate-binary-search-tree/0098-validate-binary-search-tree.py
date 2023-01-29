# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        list = []
        def inorder(root):
            nonlocal list
            if root != None:
                inorder(root.left)
                list.append(root.val)
                inorder(root.right)
        
        inorder(root)
        if len(list) == 1:
            return True
        
        for i in range(1, len(list)):
            if list[i] <= list[i - 1]:
                return False
        return True
            