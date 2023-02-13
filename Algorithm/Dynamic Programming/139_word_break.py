class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n, words = len(s), set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]


if __name__ == '__main__':
    s = "aebbbbs"
    wordDict = ["a", "aeb", "ebbbb", "s", "eb"]
    print(f"{s,wordDict}")
    print('----------Answer Below----------')
    print(Solution().wordBreak(s, wordDict))
