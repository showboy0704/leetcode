class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))+1
        a, b = ''.join(['0']*(n-len(a)))+a, ''.join(['0']*(n-len(b)))+b
        digits = ['']*n
        carry = 0
        for i in range(n-1, -1, -1):
            digit = int(a[i])+int(b[i])+carry
            carry = 0
            if digit > 1:
                carry = 1
                digit -= 2
            digits[i] = str(digit)

        return ''.join(digits) if digits[0] == '1' else ''.join(digits[1:])


if __name__ == '__main__':
    a, b = "1100000", "110"
    print(f"{a , b}")
    print('----------Answer Below----------')
    print(Solution().addBinary(a, b))
