# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        
        def preorder(root, list):
            if root != None:
                list.append(str(root.val))
                preorder(root.left, list)
                preorder(root.right, list)
            else:
                list.append("None")

        preList = []
        preorder(root, preList)
        
        return ' '.join(preList)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        
        preList = data.split(' ')
        idx = 0
        def buildTree(preList):
            nonlocal idx
            if idx >= len(preList):
                return None
            if preList[idx] == "None":
                idx += 1
                return None
            else:
                root = TreeNode(int(preList[idx]))
                idx += 1
                root.left = buildTree(preList)
                root.right = buildTree(preList)
            return root
        
        return buildTree(preList)
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))