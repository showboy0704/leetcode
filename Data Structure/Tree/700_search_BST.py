class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def preorder(node, val):
            if node:
                if node.val == val:
                    return node
                elif node.val > val:
                    return preorder(node.left, val)
                else:
                    return preorder(node.right, val)

        return preorder(root, val)
