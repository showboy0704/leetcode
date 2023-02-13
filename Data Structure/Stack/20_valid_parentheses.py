class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket = {'(': 1, '[': 2, '{': 3}
        close_bracket = {')': 1, ']': 2, '}': 3}
        stack = []
        for c in s:
            if c in close_bracket:
                if not stack:
                    return False
                if open_bracket[stack.pop()] != close_bracket[c]:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True


if __name__ == '__main__':
    s = "["
    print(f"{s}")
    print(Solution().isValid(s))
