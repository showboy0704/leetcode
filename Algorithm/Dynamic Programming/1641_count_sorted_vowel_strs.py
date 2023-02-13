class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1, 1, 1, 1, 1]
        for _ in range(1, n):
            for j in range(1, 5):
                dp[j] = dp[j]+dp[j-1]
        return sum(dp)


if __name__ == '__main__':
    n = 33
    print(f"{n}")
    print('----------Answer Below----------')
    print(Solution().countVowelStrings(n))
