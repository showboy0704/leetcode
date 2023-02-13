class Solution:
    def find(self, i, j, grid):
        if not((0 <= i < len(grid)) and (0 <= j < len(grid[0]))):
            return 0
        if grid[i][j] == 0:
            return 0

        grid[i][j] = 0
        return 1 + (self.find(i+1, j, grid)+self.find(i, j + 1, grid) +
                    self.find(i-1, j, grid)+self.find(i, j-1, grid))

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = max(area, self.find(i, j, grid))
        return area


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
        0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(f"{grid}")
    print('----------Answer Below----------')
    print(Solution().maxAreaOfIsland(grid))
