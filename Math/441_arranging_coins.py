class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)


if __name__ == '__main__':
    n = 1
    print(f"{n}")
    print('----------Answer Below----------')
    print(Solution().arrangeCoins(n))
