class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max([sum(customer) for customer in accounts])


if __name__ == '__main__':
    accounts = [[1, 5], [7, 3], [3, 5]]
    print(f"{accounts}")
    print('----------Answer Below----------')
    print(Solution().maximumWealth(accounts))
