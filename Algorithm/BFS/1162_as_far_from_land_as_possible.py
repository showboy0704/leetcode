class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n = len(grid)
        queues = [[] for _ in range(2*n-1)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queues[0].append((i, j))
        if len(queues[0]) == 0 or len(queues[0]) == n*n:
            return -1
        for d in range(2*n-2):
            queue = queues[d]
            if not queue:
                return d-1
            for i, j in queue:
                for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    c, r = i+dir[0], j+dir[1]
                    if (0 <= c < n) and (0 <= r < n) and (grid[c][r] == 0):
                        grid[c][r] = grid[i][j]+1
                        queues[d+1].append((c, r))
        return d+1


if __name__ == '__main__':
    grid = [[1, 1, 1], [1, 1, 1], [1, 1, 0]]
    print(f"{grid}")
    print('----------Answer Below----------')
    print(Solution().maxDistance(grid))
