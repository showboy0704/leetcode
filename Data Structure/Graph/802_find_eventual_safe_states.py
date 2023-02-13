class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        def dfs(node):
            if self.visited[node] == 0:
                return False
            elif self.visited[node] == 1:
                return True
            else:
                self.visited[node] = 0
                if sum([dfs(n) for n in graph[node]]) == len(graph[node]):
                    self.visited[node] = 1
                    return True
                else:
                    return False
        self.visited = [-1]*len(graph)
        for node in range(len(graph)):
            dfs(node)

        return [i for i in range(len(graph)) if self.visited[i] == 1]


if __name__ == '__main__':
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    print(f"{graph}")
    print('----------Answer Below----------')
    print(Solution().eventualSafeNodes(graph))
