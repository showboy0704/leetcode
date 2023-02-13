class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        def is_connect(start, end, visited: set, graph: list) -> bool:
            if start not in visited:
                visited.add(start)
                if start == end:
                    return True
                return any(is_connect(n, end, visited, graph) for n in graph[start])

        graph = [[] for _ in edges]
        for edge in edges:
            visited = set()
            n1, n2 = [n-1 for n in edge]
            if graph[n1] and graph[n2] and is_connect(n1, n2, visited, graph):
                return edge
            graph[n1].append(n2)
            graph[n2].append(n1)


if __name__ == '__main__':
    edges = [[1, 2], [1, 3], [1, 4], [3, 4], [1, 5]]
    print(f"{edges}")
    print('----------Answer Below----------')
    print(Solution().findRedundantConnection(edges))
