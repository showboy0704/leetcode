class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        min_dist, index = 100000, -1
        for i, pt in enumerate(points):
            if x == pt[0] and y == pt[1]:
                return i
            dist = None
            if x == pt[0]:
                dist = abs(y-pt[1])
            elif y == pt[1]:
                dist = abs(x-pt[0])
            if dist and dist < min_dist:
                min_dist, index = dist, i
        return index


if __name__ == '__main__':
    x, y, points = 3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
    print(f"{x , y , points}")
    print(Solution().nearestValidPoint(x, y, points))
