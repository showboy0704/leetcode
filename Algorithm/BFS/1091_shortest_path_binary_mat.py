class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        grid[0][0] = 1
        queue = [(0, 0, 1)]
        while queue:
            col, row, steps = queue[0]
            for dir_x in [-1, 0, 1]:
                for dir_y in [-1, 0, 1]:
                    i, j = col+dir_x, row+dir_y
                    if -1 < i < n and -1 < j < n and grid[i][j] == 0:
                        queue.append((i, j, steps+1))
                        grid[i][j] = steps+1
            queue = queue[1:]
        return grid[n-1][n-1] if grid[n-1][n-1] else -1


if __name__ == '__main__':
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    print(f"{grid}")
    print('----------Answer Below----------')
    print(Solution().shortestPathBinaryMatrix(grid))
