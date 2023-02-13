class Solution:
    def isValidBST(self, root) -> bool:
        stack = [(root, -(2**31)-1, 2**31)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            if not(lower < root.val < upper):
                return False
            stack.append((root.left, lower, root.val))
            stack.append((root.right, root.val, upper))
        return True
