# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:

        def build(array: list[int]) -> TreeNode:
            n = len(array)
            if n == 1:
                return TreeNode(array[0])
            elif n == 2:
                return TreeNode(array[0], None, TreeNode(array[1]))
            else:
                mid = int(n/2) if n % 2 == 0 else int((n-1)/2)
                return TreeNode(array[mid], build(array[:mid]), build(array[mid+1:]))

        return build(nums)


if __name__ == '__main__':
    nums = [0,1,2,3,4,5,6]
    print(f"{nums}")
    print('----------Answer Below----------')
    print(Solution().sortedArrayToBST(nums).val)
