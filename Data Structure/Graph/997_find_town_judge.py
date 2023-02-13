class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if len(trust) < n-1:
            return -1
        graph = [[] for _ in range(n)]
        for edge in trust:
            graph[edge[0]-1].append(edge[1])
        judge = -1
        for i in range(1, n+1):
            if len(graph[i-1]) == 0:
                if judge == -1:
                    judge = i
                else:
                    judge = -1
        for i in range(1, n+1):
            if judge not in graph[i-1] and judge != i:
                judge = -1
        return judge


if __name__ == '__main__':
    n, trust = 3, [[1, 3], [2, 3]]
    print(f"{n , trust }")
    print('----------Answer Below----------')
    print(Solution().findJudge(n, trust))
