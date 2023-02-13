# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.result = root

        def pre_order(node: 'TreeNode'):
            if not node:
                return False
            left = pre_order(node.left)
            right = pre_order(node.right)
            mid = node.val == p.val or node.val == q.val
            if left+mid+right >= 2:
                self.result = node
            return left or mid or right
        pre_order(root)
        return self.result
