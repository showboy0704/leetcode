class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        primes = [True]*1001
        primes[0], primes[1] = False, False
        for i in range(2, int(1001**0.5)+1):
            if primes[i]:
                for j in range(i*i, 1001, i):
                    primes[j] = False
        primes_int = []
        for i in range(1001):
            if primes[i]:
                primes_int.append(i)
        prime_set = set()
        for num in nums:
            for prime in primes_int:
                if num % prime == 0:
                    prime_set.add(prime)
        return len(prime_set)
