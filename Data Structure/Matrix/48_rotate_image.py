from copy import deepcopy
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        tmp_matrix = deepcopy(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = tmp_matrix[n-1-j][i]
        return matrix


if __name__ == '__main__':
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print(f"{matrix}")
    print('----------Answer Below----------')
    print(Solution().rotate(matrix))
