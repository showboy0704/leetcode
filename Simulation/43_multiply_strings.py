class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        num = 0
        for i in range(m):
            for j in range(n):
                num += int(num1[i])*int(num2[j])*10**(m+n-i-j-2)
        return str(num)


if __name__ == '__main__':
    num1, num2 = "123", "456"
    print(f"{num1 , num2}")
    print('----------Answer Below----------')
    print(Solution().multiply(num1, num2))
