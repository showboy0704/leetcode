# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        def build(p: list[int], i: list[int]) -> TreeNode:
            n = len(p)
            if n == 0:
                return None
            elif n == 1:
                return TreeNode(p[0])
            elif n == 2:
                if p == i:
                    return TreeNode(p[0], None, TreeNode(p[1]))
                else:
                    return TreeNode(p[0], TreeNode(p[1]), None)
            else:
                mid = p[0]
                i_left,i_right = i[:i.index(mid)],i[i.index(mid)+1:]
                p_left = p[1:1+len(i_left)]
                p_right = p[1+len(i_left):1+len(i_left)+len(i_right)]
                return TreeNode(mid, build(p_left, i_left), build(p_right, i_right))

        return build(preorder, inorder)
