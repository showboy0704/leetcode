class Solution:
    def isMatch(self, s, p):
        i, j, star = 0, 0, -1
        match = 0
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                match = i
                star = j
                j += 1
            elif star != -1:
                j = star+1
                match += 1
                i = match
            else:
                return False
        while j < len(p) and p[j] == '*':
            j +=1

        if j == len(p):
            return True
        else:
            return False


if __name__ == '__main__':
    s, p = "abcabczzzde", "*abc???de*"
    print(f"{s  , p}")
    print('----------Answer Below----------')
    print(Solution().isMatch(s, p))
