# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(arr: list) -> bool:
    return arr == arr[::-1]


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue, vals = [root], []
        while queue:
            node = queue[0]
            queue = queue[1:]

            if node:
                vals.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                vals.append(None)
        n = len(vals)
        start = 1
        l = start*2
        while start < n:
            if not is_symmetric(vals[start:start+l]):
                return False
            s = start
            start = start+l
            l = len([val for val in vals[s:s+l]
                    if val is not None])*2

        return True
