class Solution:
    def get_ops(self):
        if self.stack:
            self.num1 = int(self.stack.pop())
            self.num2 = int(self.stack.pop())
            return True
        else:
            return False

    def solve(self, operator):
        if self.get_ops():
            if operator == '+':
                self.stack.append(self.num2+self.num1)
            elif operator == '-':
                self.stack.append(self.num2-self.num1)
            elif operator == '*':
                self.stack.append(self.num2*self.num1)
            elif operator == '/':
                self.stack.append(int(self.num2/self.num1))
        else:
            return False
        return True

    def evalRPN(self, tokens: list[str]) -> int:
        self.stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                self.solve(token)
            else:
                self.stack.append(token)
        return self.stack[0]


if __name__ == '__main__':
    tokens = ["10", "6", "9", "3", "+", "-11",
              "*", "/", "*", "17", "+", "5", "+"]
    print(f"{tokens}")
    print('----------Answer Below----------')
    print(Solution().evalRPN(tokens))
