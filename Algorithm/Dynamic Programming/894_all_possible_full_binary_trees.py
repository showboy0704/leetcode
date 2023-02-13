class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    dp = {0: [],1: [TreeNode(0)]}
    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        if n not in self.dp:
            trees = []
            for i in range(1, n-1, 2):
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(n - i - 1):
                        root = TreeNode(0, left, right)
                        trees.append(root)
            self.dp[n] = trees
        return self.dp[n]
