from math import ceil, sqrt


class Solution:
    def twoEggDrop(self, n: int) -> int:
        return ceil((sqrt(1 + 8 * n) - 1) / 2)


if __name__ == '__main__':
    n = 100
    print(f"{n}")
    print('----------Answer Below----------')
    print(Solution().twoEggDrop(n))
