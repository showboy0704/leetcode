class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[] for _ in range(m)]
        grid[0] = [1 for _ in range(n)]
        for col in range(1, m):
            for row in range(n):
                if row == 0:
                    grid[col].append(1)
                else:
                    grid[col].append(grid[col][row-1]+grid[col-1][row])
        return grid[-1][-1]


if __name__ == '__main__':
    m, n = 3, 7
    print(f"{m,n}")
    print('----------Answer Below----------')
    print(Solution().uniquePaths(m, n))
