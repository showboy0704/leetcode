class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True]*n
        primes[0], primes[1] = False, False
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
        print(primes)
        return sum(primes)


if __name__ == '__main__':
    n = 100
    print(f"{n}")
    print('----------Answer Below----------')
    print(Solution().countPrimes(n))
