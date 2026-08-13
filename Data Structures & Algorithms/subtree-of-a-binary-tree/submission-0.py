# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            else:
                return sameTree(node1.left,node2.left) and sameTree(node1.right,node2.right)
        
        q = deque([root])

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if sameTree(node,subRoot):
                    return True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return False
        
    
