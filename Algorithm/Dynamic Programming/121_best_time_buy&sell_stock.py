class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_cur = max_profit = 0
        for i in range(1, len(prices)):
            max_cur = max(0, max_cur+prices[i]-prices[i-1])
            max_profit = max(max_profit, max_cur)

        return max_profit


if __name__ == '__main__':
    prices = [1,2]
    print(f"{prices  }")
    print('----------Answer Below----------')
    print(Solution().maxProfit(prices))
