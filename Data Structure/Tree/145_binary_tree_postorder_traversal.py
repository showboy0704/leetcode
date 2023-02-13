class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        def postorder(node, vals=[]):
            if node:
                vals=postorder(node.left, vals)
                vals=postorder(node.right, vals)
                vals.append(node.val)
            return vals
        return postorder(root)
