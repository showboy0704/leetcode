# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.path = []
        self.result = []

    def backtrack(self, node: TreeNode):
        if (not node.left) and (not node.right):
            self.path.append(str(node.val))
            self.result.append('->'.join(self.path))
            return
        else:
            self.path.append(str(node.val))
            if node.left:
                self.backtrack(node.left)
                self.path.pop()
            if node.right:
                self.backtrack(node.right)
                self.path.pop()

    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        self.backtrack(root)
        return self.result
