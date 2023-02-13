class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    queue = [(i, j)]
                    while queue:
                        col, row = queue[0]
                        if -1 < col < m and -1 < row < n and grid[col][row] == 1:
                            grid[col][row] = 0
                            queue.extend(
                                [(col, row+1), (col+1, row), (col-1, row), (col, row-1)])
                        queue = queue[1:]
        moves = 0
        for i in range(m):
            for j in range(n):
                queue = [(i, j)]
                while queue:
                    col, row = queue[0]
                    if -1 < col < m and -1 < row < n and grid[col][row] == 1:
                        grid[col][row] = 0
                        moves += 1
                        queue.extend([(col, row+1), (col+1, row),
                                    (col-1, row), (col, row-1)])
                    queue = queue[1:]
        return moves


if __name__ == '__main__':
    grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    print(f"{grid}")
    print('----------Answer Below----------')
    print(Solution().numEnclaves(grid))
