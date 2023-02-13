class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table = {}
        for c in magazine:
            if c not in table:
                table[c] = 1
            else:
                table[c] += 1
        for c in ransomNote:
            if c not in table:
                return False
            else:
                if table[c] == 1:
                    del table[c]
                else:
                    table[c] -= 1
        return True


if __name__ == '__main__':
    r, m = 'aa', 'aab'
    print(f"{r,m}")
    print('----------Answer Below----------')
    print(Solution().canConstruct(r, m))
