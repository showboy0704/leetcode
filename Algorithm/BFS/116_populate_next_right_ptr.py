class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if root:
            queue, h, n, node = [root], 1, 0, None
            while queue:
                pre_node = node
                node = queue[0]
                queue = queue[1:]

                if node:
                    n += 1
                    if n == 2**(h-1):
                        h += 1
                        node.next = None
                    else:
                        node.next = pre_node
                    queue.append(node.right)
                    queue.append(node.left)
        return root
