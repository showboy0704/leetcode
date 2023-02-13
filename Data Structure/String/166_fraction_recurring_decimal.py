class Solution:
    def fractionToDecimal(self, num, denominator):
        n, remainder = divmod(abs(num), abs(denominator))
        sign = '-' if num*denominator < 0 else ''
        result = [sign+str(n), '.']
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))

        idx = stack.index(remainder)
        result.insert(idx+2, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')


if __name__ == '__main__':
    num, denominator = 4, 333
    print(f"{num, denominator}")
    print('----------Answer Below----------')
    print(Solution().fractionToDecimal(num, denominator))
