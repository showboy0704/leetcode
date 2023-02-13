class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n-1:
            return -1
        graph = [[] for _ in range(n)]
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = set()
        clusters = 0
        for start in range(n):
            if start not in visited:
                clusters += 1
                stack = [start]
                while stack:
                    start = stack.pop()
                    visited.add(start)
                    stack += [c for c in graph[start] if c not in visited]
        return clusters-1


if __name__ == '__main__':
    n, roads = 6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
    print(f"{n , roads }")
    print('----------Answer Below----------')
    print(Solution().makeConnected(n, roads))
