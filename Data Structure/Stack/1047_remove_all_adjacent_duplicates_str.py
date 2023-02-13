class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)


if __name__ == '__main__':
    s = "abbaca"
    print(f"{s}")
    print(Solution().removeDuplicates(s))
