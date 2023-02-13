class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        if not root:
            return []
        nodes, stack = [], [root]
        while stack:
            node = stack[-1]
            if node.children:
                for _ in range(len(node.children)):
                    child = node.children.pop()
                    stack.append(child)
            else:
                nodes.append(node.val)
                stack.pop()

        return nodes
