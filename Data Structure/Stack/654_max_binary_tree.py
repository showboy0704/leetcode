# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode:
        if not nums:
            return None
        stack, last_node = [], None
        for num in nums:
            while stack and num > stack[-1].val:
                last_node = stack.pop()
            node = TreeNode(num)
            if stack:
                stack[-1].right = node
            if last_node:
                node.left = last_node
            stack.append(node)
            last_node = None

        return stack[0]


if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    print(f"{nums}")
    print(Solution().constructMaximumBinaryTree(nums))
