class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not (n & n - 1)


if __name__ == '__main__':
    n = 1
    print(f"{n}")
    print('----------Answer Below----------')
    print(Solution().isPowerOfTwo(n))
