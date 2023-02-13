class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(node, total=0, leaf='right'):
            if node:
                if not node.left and not node.right and leaf == 'left':
                    return total+node.val
                return dfs(node.left, total, 'left') + dfs(node.right)
            else:
                return 0

        return dfs(root)
