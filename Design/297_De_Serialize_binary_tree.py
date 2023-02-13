class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        nodes = []
        queue = [root]
        while queue:
            node = queue[0]
            queue = queue[1:]
            if node:
                nodes.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                nodes.append('#')
        return ','.join(nodes)

    def deserialize(self, data: str) -> TreeNode:
        if data == '#':
            return None
        nodes = data.split(',')
        root = TreeNode(nodes[0])
        i = 1
        queue = [root]
        while queue:
            node = queue[0]
            queue = queue[1:]
            children=[None,None]
            for j in range(2):
                if nodes[i] != '#':
                    children[j] = TreeNode(int(nodes[i]))
                    queue.append(children[j])
                i += 1

            node.left, node.right = children
        return root
