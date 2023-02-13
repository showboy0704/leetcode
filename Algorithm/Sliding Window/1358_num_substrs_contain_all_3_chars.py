class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        l = 0
        r = l+2
        table = dict(a=0, b=0, c=0)
        table[s[l]] += 1
        table[s[l+1]] += 1
        table[s[r]] += 1
        count = 0
        while l < n-2 and r < n:
            if table['a'] >= 1 and table['b'] >= 1 and table['c'] >= 1:
                count += n-r
                table[s[l]] -= 1
                l += 1
            else:
                if r+1 == n:
                    break
                r += 1
                table[s[r]] += 1
        return count


if __name__ == '__main__':
    s = "ababbbc"
    print(f"{s}")
    print('----------Answer Below----------')
    print(Solution().numberOfSubstrings(s))
