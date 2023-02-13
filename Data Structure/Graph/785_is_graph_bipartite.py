from collections import deque


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        def bfs(source, graph):
            queue = deque([source])
            color[source] = 0
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == color[node]:
                        return False
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)

            return True
        n = len(graph)

        color = [-1] * n
        for i in range(n):
            if color[i] == -1:
                if not bfs(i, graph):
                    return False
        return True


if __name__ == '__main__':
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    print(f"{graph }")
    print('----------Answer Below----------')
    print(Solution().isBipartite(graph))
