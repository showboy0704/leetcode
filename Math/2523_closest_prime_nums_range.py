class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        primes = [True]*(right+1)
        primes[0], primes[1] = False, False
        for i in range(2, int((right+1)**0.5)+1):
            if primes[i]:
                for j in range(i*i, (right+1), i):
                    primes[j] = False
        primes_int = []
        for i in range(left, right+1):
            if primes[i]:
                primes_int.append(i)
        if len(primes_int) < 2:
            return[-1, -1]
        mini = right+1
        result = []
        for i in range(1, len(primes_int)):
            if (primes_int[i] - primes_int[i-1]) < mini:
                mini = primes_int[i] - primes_int[i-1]
                result = primes_int[i-1:i+1]
        return result
