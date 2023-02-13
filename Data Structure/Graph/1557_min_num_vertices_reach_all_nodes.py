class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        reachables = [False]*n
        for _, end in edges:
            reachables[end] = True
        return [i for i in range(n) if not reachables[i]]


if __name__ == '__main__':
    n, edges = 8, [[0,1],[2,1],[3,1],[1,4],[2,4]]
    print(f"{n,edges}")
    print('----------Answer Below----------')
    print(Solution().findSmallestSetOfVertices(n, edges))
