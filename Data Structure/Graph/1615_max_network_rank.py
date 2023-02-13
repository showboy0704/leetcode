class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]
        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
        _max = 0
        for i in range(n):
            for j in range(i+1, n):
                paths = set()
                for end in graph[i]:
                    path = [i, end]
                    path.sort()
                    paths.add(tuple(path))
                for end in graph[j]:
                    path = [j, end]
                    path.sort()
                    paths.add(tuple(path))
                _max = max(_max, len(paths))
        return _max


if __name__ == '__main__':
    n, roads = 4, [[0, 1], [0, 3], [1, 2], [1, 3]]
    print(f"{n, roads }")
    print('----------Answer Below----------')
    print(Solution().maximalNetworkRank(n, roads))
