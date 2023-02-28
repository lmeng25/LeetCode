"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        def dfs(node):
            if not node:
                return None
            if node.val in visited:
                return visited[node.val]
            copy = Node(node.val, [])
            visited[node.val] = copy
            if node.neighbors:
                for n in node.neighbors:
                    copy.neighbors.append(dfs(n))
            return copy
        
        return dfs(node)
            