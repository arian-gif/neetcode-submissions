"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.check = {}
        
        def dfs(node):
            if node in self.check:
                return self.check[node]
            copy = Node(node.val)
            self.check[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
        if not node:
            return None
        return dfs(node)
            
            