class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        m, n = len(image), len(image[0])
        queue, table = [(sr, sc)], {}
        pre_color = image[sr][sc]
        while queue:
            r, c = queue[0]
            if -1 < r < m and -1 < c < n and image[r][c] == pre_color and (r, c) not in table:
                image[r][c] = color
                table[(r, c)] = True
                queue.extend([(r, c+1), (r+1, c), (r-1, c), (r, c-1)])
            queue = queue[1:]
        return image


if __name__ == '__main__':
    image, sr, sc, color = [[0, 0, 0], [0, 0, 0]], 0, 0, 0
    print(f"{image, sr, sc, color}")
    print('----------Answer Below----------')
    print(Solution().floodFill(image, sr, sc, color))
