# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        bfs = []
        level = 0        
        q = [(root, level)]
        while q:
            tempNode = q[0][0]
            currLevel = q.pop(0)[1]
            if currLevel == len(bfs):
                bfs.append([tempNode.val])
            else:
                bfs[-1].append(tempNode.val)
            
            if tempNode.left:
                q.append((tempNode.left, currLevel + 1))
            if tempNode.right:
                q.append((tempNode.right, currLevel + 1))
        
        return [level[-1] for level in bfs]
            
        