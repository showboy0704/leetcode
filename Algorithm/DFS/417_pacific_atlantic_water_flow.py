class Solution:
    def find(self, i, j, h, grid, ocean):
        if ocean == 'paci' and (i == -1 or j == -1):
            return True
        if ocean == 'atla' and (i == len(grid) or j == len(grid[0])):
            return True
        if not((0 <= i < len(grid)) and (0 <= j < len(grid[0]))):
            return False
        if grid[i][j] > h:
            return False
        elif grid[i][j] <= h:
            if (i,j) not in self.visited:
                self.visited.add((i,j))
                return (self.find(i+1, j, grid[i][j], grid, ocean) or self.find(i, j + 1, grid[i][j], grid, ocean) or
                        self.find(i-1, j, grid[i][j], grid, ocean) or self.find(i, j-1, grid[i][j], grid, ocean))

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        pacis = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                self.visited = set()
                if self.find(i, j, 100000, heights, 'paci'):
                    pacis.append([i, j])
        result = []
        for i, j in pacis:
            self.visited = set()
            if self.find(i, j, 100000, heights, 'atla'):
                result.append([i, j])
        return result


if __name__ == '__main__':
    heights = [[1, 1], [1, 1], [1, 1]]
    print(f"{heights}")
    print('----------Answer Below----------')
    print(Solution().pacificAtlantic(heights))
