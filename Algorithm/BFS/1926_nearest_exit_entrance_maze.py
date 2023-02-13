class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m, n = len(maze), len(maze[0])
        r, c = entrance
        queue = [(r, c, 0)]
        while queue:
            r, c, steps = queue[0]
            if -1 < r < m and -1 < c < n:
                if maze[r][c] == '.':
                    maze[r][c] = steps
                    if steps != 0 and (r == 0 or r == m-1 or c == 0 or c == n-1):
                        return steps
                    queue.extend([(r, c+1, steps+1), (r+1, c, steps+1),
                                (r-1, c, steps+1), (r, c-1, steps+1)])
            queue = queue[1:]
        return -1


if __name__ == '__main__':
    maze, entrance = [["+", "+", ".", "+"],
                    [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]
    print(f"{maze, entrance}")
    print('----------Answer Below----------')
    print(Solution().nearestExit(maze, entrance))
