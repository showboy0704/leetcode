class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        if n % 3 == 0:
            return self.isPowerOfThree(n//3)


if __name__ == '__main__':
    n = 27
    print(f"{n }")
    print('----------Answer Below----------')
    print(Solution().isPowerOfThree(n))
