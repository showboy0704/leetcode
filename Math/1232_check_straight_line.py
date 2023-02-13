def get_line(coord1, coord2):
    if (coord1[0]-coord2[0]) == 0:
        return(float('inf'), coord1[0])
    m = (coord1[1]-coord2[1])/(coord1[0]-coord2[0])
    b = coord1[1]-m*coord1[0]
    return (m, b)


class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        n = len(coordinates)
        m, b = get_line(coordinates[0], coordinates[1])
        for i in range(2, n):
            if (m, b) != get_line(coordinates[0], coordinates[i]):
                return False
        return True


if __name__ == '__main__':
    coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    print(f"{coordinates}")
    print('----------Answer Below----------')
    print(Solution().checkStraightLine(coordinates))
