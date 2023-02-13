class Solution:
    def tribonacci(self, n: int) -> int:
        tribs = [0, 1, 1]
        for i in range(3, n+1):
            tribs.append(tribs[i-1]+tribs[i-2]+tribs[i-3])
        return tribs[n]


if __name__ == '__main__':
    n = 2
    print(f"{n}")
    print('----------Answer Below----------')
    print(Solution().tribonacci(n))
