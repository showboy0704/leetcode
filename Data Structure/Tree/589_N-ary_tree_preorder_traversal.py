# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        result = []
        if root:
            stack = [root]
            while stack:
                root = stack.pop()
                result.append(root.val)
                while root.children:
                    stack.append(root.children.pop())
        return result
