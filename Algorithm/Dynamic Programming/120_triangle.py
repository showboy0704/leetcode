class Solution:
    def minimumTotal(self, tri: list[list[int]]) -> int:
        memo = tri[len(tri)-1]
        for i in range(len(tri)-2, -1, -1):
            for j in range(i+1):
                memo[j] = min(tri[i][j] + memo[j],tri[i][j] + memo[j+1])
        return memo[0]


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(f"{triangle}")
    print('----------Answer Below----------')
    print(Solution().minimumTotal(triangle))
