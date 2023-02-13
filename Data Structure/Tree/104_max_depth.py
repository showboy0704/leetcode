# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node: 'TreeNode', depth):
            if node:
                dep_l = dfs(node.left, depth+1)
                dep_r = dfs(node.right, depth+1)
                return max(dep_l, dep_r)
            return depth

        return dfs(root, 0)
