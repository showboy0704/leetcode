class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1:
            return 1
        if x == 0:
            return 0
        result = 1
        if n < 0:
            x, n = 1/x, -n
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2
        return result


if __name__ == '__main__':
    x, n = 2, 4
    print(f"{x , n}")
    print('----------Answer Below----------')
    print(Solution().myPow(x, n))
