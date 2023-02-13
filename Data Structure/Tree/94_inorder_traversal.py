# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        self.result=[]
        def inorder(node: 'TreeNode'):
            if node:
                inorder(node.left)
                self.result.append(node.val)
                inorder(node.right)
            return
        inorder(root)
        return self.result
