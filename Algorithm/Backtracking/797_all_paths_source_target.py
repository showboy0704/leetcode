class Solution:
    def __init__(self) -> None:
        self.path = []
        self.result = []

    def backtrack(self, i, graph):
        self.path.append(i)
        if i == len(graph)-1:
            self.result.append(self.path[:])
            return
        for node in graph[i]:
            self.backtrack(node, graph)
            self.path.pop()
        return

    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        self.backtrack(0, graph)
        return self.result


if __name__ == '__main__':
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    print(f"{graph}")
    print('----------Answer Below----------')
    print(Solution().allPathsSourceTarget(graph))
