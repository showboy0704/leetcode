def get_slope(p1, p2):
    return ((p2[1] - p1[1]) / (p2[0] - p1[0])) if p1[0] != p2[0] else float('inf')


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        result = 1
        for i in range(len(points)):
            slopes, max_points = {}, 1
            for j in range(i + 1, len(points)):
                slope = get_slope(points[i], points[j])
                slopes[slope] = 1 if slope not in slopes else slopes[slope] + 1
                max_points = max(max_points, 1 + slopes[slope])
            result = max(result, max_points)
        return result


if __name__ == '__main__':
    points = [[-6, -1], [3, 1], [12, 3]]
    print(f"{points}")
    print('----------Answer Below----------')
    print(Solution().maxPoints(points))
