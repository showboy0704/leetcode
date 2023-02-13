class Solution:
    def find(self, i, j, grid):
        if not((0 <= i < len(grid)) and (0 <= j < len(grid[0]))):
            return False
        if grid[i][j] == 0:
            return False

        grid[i][j] = 0
        self.find(i+1, j, grid)
        self.find(i, j + 1, grid)
        self.find(i-1, j, grid)
        self.find(i, j-1, grid)
        return True

    # Fill Out of Bound Lands
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j]==0 and grid2[i][j]==1:
                    self.find(i, j, grid2)
        result = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if self.find(i, j, grid2):
                    result += 1
        return result


if __name__ == '__main__':
    grid1, grid2 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]], [
        [1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
    print(f"{grid1, grid2}")
    print(Solution().countSubIslands(grid1, grid2))
