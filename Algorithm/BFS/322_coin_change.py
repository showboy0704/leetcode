class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        visited = set()
        visited.add(amount)
        coins.sort(reverse=True)
        queue = [(amount, 1)]
        while queue:
            amount, height = queue[0]
            queue = queue[1:]
            for coin in coins:
                new_amt = amount-coin
                if new_amt in coins:
                    return height+1
                elif new_amt > 0 and new_amt not in visited:
                    queue.append((new_amt, height+1))
                    visited.add(new_amt)

        return -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 100
    print(f"{coins,amount }")
    print('----------Answer Below----------')
    print(Solution().coinChange(coins, amount))
