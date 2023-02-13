class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        first, second = cost[0], cost[1]
        for i in range(2, len(cost)):
            min_cost = cost[i]+min(first, second)
            first, second = second, min_cost

        return min(first, second)


if __name__ == '__main__':
    cost = [10, 15, 20]
    print(f"{cost}")
    print('----------Answer Below----------')
    print(Solution().minCostClimbingStairs(cost))
