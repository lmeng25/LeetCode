# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findAncestor(root, target, list):
            if root == None:
                return False
            if root.val == target.val:
                list.append(root)
                return True
            if findAncestor(root.left, target, list) or findAncestor(root.right, target, list):
                list.append(root)
                return True
            return False
            
        ansP = []
        ansQ = []
        
        findAncestor(root, p, ansP)
        findAncestor(root, q, ansQ)
        
        for node in ansP:
            for node2 in ansQ:
                if node == node2:
                    return node
        