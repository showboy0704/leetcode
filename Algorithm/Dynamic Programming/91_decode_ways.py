class Solution:
    def numDecodings(self, s: str) -> int:
        dp, dp1, dp2, n = 0, 1, 0, len(s)
        for i in range(n-1, -1, -1):
            if s[i] != '0':
                dp += dp1
            if i+1 < n and (s[i] == '1' or s[i] == '2' and s[i+1] <= '6'):
                dp += dp2
            dp, dp1, dp2 = 0, dp, dp1
        return dp1

if __name__ == '__main__':
    s = "1"
    print(f"{s}")
    print('----------Answer Below----------')
    print(Solution().numDecodings(s))
