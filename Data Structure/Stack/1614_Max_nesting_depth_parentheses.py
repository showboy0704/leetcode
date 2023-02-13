class Solution:
    def maxDepth(self, s: str) -> int:
        depth, bal = 0, 0
        for c in s:
            if c == '(':
                bal += 1
                depth = max(depth, bal)
            elif c == ')':
                bal -= 1
        return depth


if __name__ == '__main__':
    s = "(1+(2*3)+((8)/4))+1"
    print(f"{s}")
    print(Solution().maxDepth(s))
