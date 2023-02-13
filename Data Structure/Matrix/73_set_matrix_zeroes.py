class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        zeros_i, zeros_j = dict(), dict()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if not zeros_i.get(i):
                        zeros_i[i] = True
                    if not zeros_j.get(j):
                        zeros_j[j] = True
                else:
                    if zeros_i.get(i):
                        matrix[i][j] = 0
                    if zeros_j.get(j):
                        matrix[i][j] = 0
        if zeros_i:
            for i in range(max(zeros_i.keys())+1):
                for j in range(max(zeros_j.keys())+1):
                    if matrix[i][j] != 0:
                        if zeros_i.get(i):
                            matrix[i][j] = 0
                        if zeros_j.get(j):
                            matrix[i][j] = 0
        print(matrix)


if __name__ == '__main__':
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print(f"{matrix}")
    print('----------Answer Below----------')
    print(Solution().setZeroes(matrix))
