# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {}
        for i in range(len(inorder)):
            idx[inorder[i]] = i
        self.pre = 0

        def build(left,right):
            if left>right:
                return None
            val = preorder[self.pre]
            self.pre +=1
            root= TreeNode(val)
            mid = idx[val]
            root.left=build(left,mid-1)
            root.right=build(mid+1,right)
            return root
        return build(0,len(inorder)-1)
        
        # if not preorder or not inorder:
        #     return None
        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        # root.right= self.buildTree(preorder[mid+1:],inorder[mid+1:])
        # return root
        
        
        