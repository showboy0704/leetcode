from collections import deque


class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        def bfs(source):
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

        graph = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])

        color = [-1] * (n + 1)
        for i in range(1, n + 1):
            if color[i] == -1:
                if not bfs(i):
                    return False
        return True


if __name__ == '__main__':
    n, dislikes = 4, [[1, 2], [1, 3], [2, 4]]
    print(f"{n , dislikes }")
    print('----------Answer Below----------')
    print(Solution().possibleBipartition(n, dislikes))
