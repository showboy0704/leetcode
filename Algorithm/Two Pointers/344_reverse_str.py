class Solution:
    def reverseString(self, s: list[str]) -> None:
        n = len(s)
        i, j = 0, n-1
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        print(s)


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    print(f"{s }")
    print('----------Answer Below----------')
    print(Solution().reverseString(s))
