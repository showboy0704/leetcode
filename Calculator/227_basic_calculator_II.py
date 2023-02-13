class Solution:
    def calculate(self, s: str) -> int:
        num, oper, last, result = '', '+', 0, 0
        for c in s+'+':
            if not(c.isdigit() or c.isspace()):
                if oper == '+':
                    result += last
                    last = int(num)
                elif oper == '-':
                    result += last
                    last = -int(num)
                elif oper == '*':
                    last *= int(num)
                elif oper == '/':
                    last = int(last/int(num))
                num, oper = '', c
            elif c.isdigit():
                num += c
        return result+last


if __name__ == '__main__':
    s = "14-3/2"
    print(f"{s}")
    print('----------Answer Below----------')
    print(Solution().calculate(s))
