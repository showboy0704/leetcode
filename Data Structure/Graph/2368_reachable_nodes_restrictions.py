class Solution:
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        ban = {}
        for rest in restricted:
            ban[rest] = True
        graph = [[] for _ in range(n)]
        for edge in edges:
            if not (edge[0] in ban or edge[1] in ban):
                graph[edge[0]].append(edge[1])
                graph[edge[1]].append(edge[0])
        visited = set()
        stack = [0]
        while stack:
            start = stack.pop()
            visited.add(start)
            stack += [c for c in graph[start] if c not in visited]
        return len(visited)


if __name__ == '__main__':
    n, edges, restricted = 7, [[0, 1], [0, 2], [
        0, 5], [0, 4], [3, 2], [6, 5]], [4, 2, 1]
    print(f"{n, edges,restricted }")
    print('----------Answer Below----------')
    print(Solution().reachableNodes(n, edges, restricted))
