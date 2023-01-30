# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -math.inf

        def maxContribute(node):
            nonlocal res
            if node == None:
                return 0
            leftGain = max(maxContribute(node.left), 0)
            rightGain = max(maxContribute(node.right), 0)
            res = max(res, leftGain + node.val, rightGain + node.val, leftGain + node.val + rightGain)
            return max(leftGain + node.val, rightGain + node.val)
        
        maxContribute(root)
        return res