class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = dict()
        n = len(s)
        for c in s:
            if c not in table:
                table[c] = 1
            else:
                table[c] += 1
        for i in range(n):
            if table[s[i]] == 1:
                return i
        return -1


if __name__ == '__main__':
    s = "acaadcad"
    print(f"{s}")
    print('----------Answer Below----------')
    print(Solution().firstUniqChar(s))
