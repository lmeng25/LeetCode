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
        
        def dfs(node, visited):
            if not node:
                return None

            val = node.val
            if val in visited:
                return visited[val]
            
            copy = Node(val)
            visited[val] = copy
                
            if node.neighbors:
                copy.neighbors = []
                for neighbor in node.neighbors:
                    copy.neighbors.append(dfs(neighbor, visited))
            
            return copy
        
        return dfs(node, visited)