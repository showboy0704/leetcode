class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat
        mat_re = [[0]*c for _ in range(r)]
        for i in range(m):
            for j in range(n):
                mat_re[(i*n+j)//c][(i*n+j) % c] = mat[i][j]
        return mat_re


if __name__ == '__main__':
    mat, r, c = [[1, 2], [3, 4]], 1, 4
    print(f"{mat, r, c}")
    print('----------Answer Below----------')
    print(Solution().matrixReshape(mat, r, c))
