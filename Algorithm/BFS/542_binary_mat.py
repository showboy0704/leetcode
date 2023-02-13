class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        queues, visited = [], []
        for i in range(m):
            visited.append([])
            for j in range(n):
                queues.append([])
                visited[i].append(False)
                if mat[i][j] == 0:
                    visited[i][j] = True
                    queues[0].append((i, j))
        for d in range(m+n-2):
            queue = queues[d]
            for i, j in queue:
                for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    c, r = i+dir[0], j+dir[1]
                    if (0 <= c < m) and (0 <= r < n) and (not visited[c][r]):
                        mat[c][r] = mat[i][j]+1
                        visited[c][r] = True
                        queues[d+1].append((c, r))
        return mat


if __name__ == '__main__':
    mat = [[0, 0, 0, 1], [0, 1, 0, 1], [0, 0, 0, 1]]
    print(f"{mat}")
    print('----------Answer Below----------')
    print(Solution().updateMatrix(mat))
