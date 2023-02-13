# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode:
        mid = None
        root = TreeNode(preorder[0])
        stack = [root]
        for val in preorder[1:]:
            while stack and val > stack[-1].val:
                mid = stack.pop()
            node = TreeNode(val)
            if mid:
                mid.right = node
            else:
                if stack:
                    stack[-1].left = node
            stack.append(node)
            mid = None
        return root


if __name__ == '__main__':
    preorder = [100, 90, 80, 70, 60, 75, 85, 95, 105]
    print(f"{preorder}")
    print('----------Answer Below----------')
    print(Solution().bstFromPreorder(preorder))
