class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes = 0
        while n != 0:
            n //=5
            zeroes += n
        return zeroes


if __name__ == '__main__':
    n = 125
    print(f"{n}")
    print('----------Answer Below----------')
    print(Solution().trailingZeroes(n))
