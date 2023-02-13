class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def search(root, val):
            if root:
                if root.val == val:
                    return True
                elif root.val > val:
                    return search(root.left, val)
                else:
                    return search(root.right, val)

        def preorder(root, node, k):
            if node:
                if search(root, k-node.val) and node.val*2 != k:
                    return True
                return preorder(root, node.left, k) or preorder(root, node.right, k)
        if preorder(root, root, k):
            return True
        return False
