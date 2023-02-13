from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue, freshes = deque(), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    freshes += 1
        if freshes == 0:
            return 0

        while queue:
            r, c = queue.popleft()
            for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                i, j = r+dir[0], c+dir[1]
                if -1 < i < m and -1 < j < n and grid[i][j] == 1:
                    freshes -= 1
                    grid[i][j] = grid[r][c]+1
                    if freshes == 0:
                        return grid[i][j]-2
                    queue.append((i, j))
        return -1


if __name__ == '__main__':
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(f"{grid}")
    print('----------Answer Below----------')
    print(Solution().orangesRotting(grid))
