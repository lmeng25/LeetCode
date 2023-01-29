# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return res
        
        stack = []
        stack.append([root, 0])
        level = 0
        
        while stack:
            temp = stack.pop(0)
            if len(res) == 0:
                res.append([temp[0].val])
            elif level != temp[1]:
                res.append([temp[0].val])
                level += 1
            else:
                res[-1].append(temp[0].val)
                
            if temp[0].left != None:
                stack.append([temp[0].left, temp[1] + 1])
            if temp[0].right != None:
                stack.append([temp[0].right, temp[1] + 1])
        
        return res
        