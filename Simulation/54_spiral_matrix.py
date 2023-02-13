class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        if m == 1:
            return matrix[0]
        side, i, j = 1, 0, 0
        result = []
        while matrix[i][j] != '#':
            result.append(matrix[i][j])
            matrix[i][j] = '#'
            if side % 4 == 1:
                j += 1
                if j == n-side//4:
                    side += 1
                    j -= 1
                    i += 1
            elif side % 4 == 2:
                i += 1
                if i == m-side//4:
                    side += 1
                    i -= 1
                    j -= 1
            elif side % 4 == 3:
                j -= 1
                if j == -1+side//4:
                    side += 1
                    j += 1
                    i -= 1
            else:
                i -= 1
                if i == -1+side//4:
                    side += 1
                    i += 1
                    j += 1

        return result


if __name__ == '__main__':
    matrix = [[1]]
    print(f"{matrix}")
    print('----------Answer Below----------')
    print(Solution().spiralOrder(matrix))
