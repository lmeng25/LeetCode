# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorderIndex = 0
        
        def arrayToTree(start, end):
            nonlocal preorderIndex
            if end < start:
                return None
            rootVal = preorder[preorderIndex]
            preorderIndex += 1
            root = TreeNode(rootVal)
            root.left = arrayToTree(start, inorder.index(rootVal) - 1)
            root.right = arrayToTree(inorder.index(rootVal) + 1, end)
            return root
        
        return arrayToTree(0, len(inorder) - 1)