class Solution:
    table = dict(I=1, IV=4, V=5, IX=9, X=10, XL=40, L=50,
                XC=90, C=100, CD=400, D=500, CM=900, M=1000)

    def romanToInt(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return self.table[s]
        l = num = 0
        while l < n:
            c = s[l:l+2]
            if c in self.table:
                num += self.table[c]
                l+=1
            else:
                num += self.table[c[0]]
            l += 1
        return num


if __name__ == '__main__':
    s = "III"
    print(f"{s }")
    print('----------Answer Below----------')
    print(Solution().romanToInt(s))
