# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        def preorder(node):
            if not node:
                result.append("#")
                return 
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        sol = ""
        for i, res in enumerate(result):
            if i>0:
                sol+=","
            sol+=res
        return sol


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = data.split(",")
        self.i = 0

        def build():
            val = tokens[self.i]
            self.i += 1
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        return build()
        
