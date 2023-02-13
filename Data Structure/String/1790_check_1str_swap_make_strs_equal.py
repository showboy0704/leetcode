class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        chars1, chars2 = [], []
        for i in range(n):
            if s1[i] != s2[i]:
                chars1.append(s1[i])
                chars2.append(s2[i])
            if len(chars1) > 2:
                return False
        if len(chars1) == 0:
            return True
        if len(chars1) == 1:
            return False
        if len(chars1) == 2 and chars1[::-1] == chars2:
            return True


if __name__ == '__main__':
    s1, s2 = "aa", "bb"
    print(f"{s1 , s2}")
    print(Solution().areAlmostEqual(s1, s2))
