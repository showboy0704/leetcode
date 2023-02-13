class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        queue, stack = [], []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    stack.append((i, j))
                    queue.append((i, j))
                    break
            if stack:
                break
        while stack:
            col, row = stack.pop()
            for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                i, j = col+dir[0], row+dir[1]
                if -1 < i < n and -1 < j < n and grid[i][j] == 1:
                    stack.append((i, j))
                    queue.append((i, j))
                    grid[i][j] = 2
        while queue:
            col, row = queue[0]
            for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                i, j = col+dir[0], row+dir[1]
                if -1 < i < n and -1 < j < n:
                    if grid[i][j] == 1:
                        return grid[col][row]-2
                    elif grid[i][j] == 0:
                        queue.append((i, j))
                        grid[i][j] = grid[col][row]+1
            queue = queue[1:]


if __name__ == '__main__':
    grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
    print(f"{grid}")
    print('----------Answer Below----------')
    print(Solution().shortestBridge(grid))
