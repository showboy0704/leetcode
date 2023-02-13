class Solution:
    def find(self, i, j, grid):
        if not((0 <= i < len(grid)) and (0 <= j < len(grid[0]))):
            return False
        if grid[i][j] == 1:
            return False

        grid[i][j] = 1
        self.find(i+1, j, grid)
        self.find(i, j + 1, grid)
        self.find(i-1, j, grid)
        self.find(i, j-1, grid)
        return True

    def closedIsland(self, grid: list[list[str]]) -> int:
        # Fill Boundary Islands
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0])-1:
                    self.find(i, j, grid)
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.find(i, j, grid):
                    result += 1
        return result


if __name__ == '__main__':
    grid = [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0, 1, 1, 1, 0], [
        1, 0, 1, 1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]]
    print(f"{grid}")
    print(Solution().closedIsland(grid))
