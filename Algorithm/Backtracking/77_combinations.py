class Solution:
    def backtrack(self, dim: int, n, k):
        if dim == k:
            self.results.append(self.result[:])
            return

        for i in range(dim+1, n+1):
            if not self.result or i > self.result[-1]:
                self.result.append(i)
                self.backtrack(dim+1, n, k)
                self.result.pop()

    def combine(self, n: int, k: int) -> list[list[int]]:
        self.result = []
        self.results = []
        if k:
            self.backtrack(0, n, k)
        return self.results


if __name__ == '__main__':
    n, k = 4, 2
    print(f"{n , k}")
    print('----------Answer Below----------')
    print(Solution().combine(n, k))
