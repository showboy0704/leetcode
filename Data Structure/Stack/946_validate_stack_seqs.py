class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        n = len(pushed)
        i = j = 0
        for _ in range(2*n):
            if not stack:
                stack.append(pushed[i])
                i += 1
            else:
                if stack and popped[j] != stack[-1]:
                    if i == n:
                        break
                    stack.append(pushed[i])
                    i += 1
                else:
                    if j == n:
                        break
                    stack.pop()
                    j += 1

        if stack:
            return False
        return True


if __name__ == '__main__':
    pushed, popped = [1, 2, 3, 4, 5],  [4, 5, 3, 2, 1]
    print(f"{pushed, popped}")
    print(Solution().validateStackSequences(pushed, popped))
