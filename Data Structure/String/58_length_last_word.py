class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        count = 0
        while s[i] == ' ':
            i -= 1
        while 0 <= i and s[i] != ' ':
            i -= 1
            count += 1

        return count


if __name__ == '__main__':
    s = "a"
    print(f"{s}")
    print('----------Answer Below----------')
    print(Solution().lengthOfLastWord(s))
