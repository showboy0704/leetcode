class Solution:
    def find(self, i, j):
        if not((0 <= i < len(self.grid)) and (0 <= j < len(self.grid[0]))):
            return False
        if self.grid[i][j] == '0':
            return False

        self.grid[i][j] = '0'
        self.find(i+1, j)
        self.find(i, j + 1)
        self.find(i-1, j)
        self.find(i, j-1)
        return True

    def numIslands(self, grid: list[list[str]]) -> int:
        self.grid = grid
        self.result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.find(i, j):
                    self.result += 1
        return self.result


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(f"{grid}")
    print(Solution().numIslands(grid))
