class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        power = len(columnTitle)-1
        num = 0
        for c in columnTitle:
            num += (ord(c)-64)*26**power
            power -= 1
        return num


if __name__ == '__main__':
    columnTitle = "AB"
    print(f"{columnTitle}")
    print('----------Answer Below----------')
    print(Solution().titleToNumber(columnTitle))
