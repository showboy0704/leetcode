class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        return edges[1][0] if edges[1][0] in edges[0] else edges[1][1]


if __name__ == '__main__':
    edges = [[1, 2], [5, 1], [1, 3], [1, 4]]
    print(f"{edges}")
    print('----------Answer Below----------')
    print(Solution().findCenter(edges))
