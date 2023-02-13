class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        conn = [0]*n
        for road in roads:
            conn[road[0]] += 1
            conn[road[1]] += 1
        conn.sort()
        return sum([(i+1)*conn[i] for i in range(n)])


if __name__ == '__main__':
    n, roads = 5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
    print(f"{n , roads }")
    print('----------Answer Below----------')
    print(Solution().maximumImportance(n, roads))
