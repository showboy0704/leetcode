class Solution:
    def __init__(self) -> None:
        self.results = []

    def backtrack(self, brackets=[], left=0, right=0):
        if len(brackets) == 2*self.n:
            self.results.append("".join(brackets))
            return

        if left < self.n:
            brackets.append("(")
            self.backtrack(brackets, left+1, right)
            brackets.pop()
        if right < left:
            brackets.append(")")
            self.backtrack(brackets, left, right+1)
            brackets.pop()

    def generateParenthesis(self, n: int) -> list[str]:
        self.n = n
        self.backtrack()
        return self.results


if __name__ == '__main__':
    n = 3
    print(f"{n}")
    print('----------Answer Below----------')
    print(Solution().generateParenthesis(n))
