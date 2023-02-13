class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = [i for i in range(1, n+1)]
        for mod in range(n, 1, -1):
            steps = k % mod
            if steps == 0:
                steps = mod
            counted = queue[:steps-1]
            queue = queue[steps:]
            queue.extend(counted)
        return queue[0]


if __name__ == '__main__':
    n, k = 6, 6
    print(f"{n,k}")
    print('----------Answer Below----------')
    print(Solution().findTheWinner(n, k))
