class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank = start = 0
        for i in range(len(gas)):
            tank += gas[i]-cost[i]
            if tank < 0:
                tank, start = 0, i+1
        return start


if __name__ == '__main__':
    gas, cost = [1, 2, 3, 4, 5], [3, 4, 5, 1, 2]
    print(f"{gas , cost}")
    print('----------Answer Below----------')
    print(Solution().canCompleteCircuit(gas, cost))
