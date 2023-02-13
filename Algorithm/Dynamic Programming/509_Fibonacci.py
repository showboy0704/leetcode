class Solution:
    def fib(self, n: int) -> int:
        fibs = [0, 1]
        for i in range(2, n+1):
            fibs.append(fibs[i-1]+fibs[i-2])
        return fibs[n]


if __name__ == '__main__':
    n = 2
    print(f"{n}")
    print('----------Answer Below----------')
    print(Solution().fib(n))
