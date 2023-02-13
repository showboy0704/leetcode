class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def preorder(node, total, target):
            if node:
                total += node.val
                if not node.left and not node.right:
                    if total == target:
                        return True
                    else:
                        return False
                if preorder(node.left, total, target) or preorder(node.right, total, target):
                    return True

        if preorder(root, 0, targetSum):
            return True
        return False
