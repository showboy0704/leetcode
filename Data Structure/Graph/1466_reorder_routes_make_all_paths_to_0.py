class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]
        for edge in connections:
            n1, n2 = edge
            graph[n1].append(n2)
            graph[n2].append(n1)

        num = 0
        paths, visited = set(), set()
        stack = [0]
        while stack:
            start = stack.pop()
            visited.add(start)
            no_visited = [c for c in graph[start] if c not in visited]
            for end in no_visited:
                paths.add((start, end))
            stack.extend(no_visited)
        for edge in connections:
            if tuple(edge) in paths:
                num += 1
        return num


if __name__ == '__main__':
    n, connections = 6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    print(f"{n , connections}")
    print('----------Answer Below----------')
    print(Solution().minReorder(n, connections))
