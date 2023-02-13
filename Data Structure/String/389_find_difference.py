class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        table = {}
        for c in t:
            if c in table:
                table[c] += 1
            else:
                table[c] = 1
        for c in s:
            table[c] -= 1
            if table[c] == 0:
                del table[c]
        return list(table.keys())[0]


if __name__ == '__main__':
    s, t = "abcd", "abcde"
    print(f"{s , t}")
    print('----------Answer Below----------')
    print(Solution().findTheDifference(s, t))
