class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        def preorder(node, vals=[]):
            if node:
                vals.append(node.val)
                vals = preorder(node.left, vals)
                vals = preorder(node.right, vals)
            return vals
        return preorder(root)
