class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        graph = [[[], []] for _ in range(n)]
        for i, j in redEdges:
            graph[i][0].append(j)
        for i, j in blueEdges:
            graph[i][1].append(j)
        answer = [[0, 0]] + [[n * 2, n * 2] for _ in range(n - 1)]
        queue = [[0, 0], [0, 1]]
        for i, color in queue:
            for j in graph[i][color]:
                if answer[j][color] == n * 2:
                    answer[j][color] = answer[i][1 - color] + 1
                    queue.append([j, 1 - color])
        return [x if x < n * 2 else -1 for x in map(min, answer)]


if __name__ == '__main__':
    n, redEdges, blueEdges = 3, [[0, 1], [1, 2]], []
    print(f"{n , redEdges , blueEdges }")
    print('----------Answer Below----------')
    print(Solution().shortestAlternatingPaths(n, redEdges, blueEdges))
