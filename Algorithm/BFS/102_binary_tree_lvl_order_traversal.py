class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        result = []
        if root:
            queue,lvl_vals = [root],[]
            cur_lvl_lim, next_lvl_lim = 1, 0
            while queue:
                node = queue[0]
                queue = queue[1:]
                cur_lvl_lim -= 1
                if node:
                    next_lvl_lim += 2
                    lvl_vals.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                if cur_lvl_lim == 0:
                    if lvl_vals:
                        result.append(lvl_vals)
                    lvl_vals=[]
                    cur_lvl_lim = next_lvl_lim
                    next_lvl_lim = 0
        return result
