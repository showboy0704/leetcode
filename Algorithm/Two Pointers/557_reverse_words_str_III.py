class Solution:
    def reverseWords(self, s: str) -> str:
        chars = []
        end = -1
        for i in range(len(s)):
            if s[i] == ' ':
                for j in range(i-1, end, -1):
                    chars.append(s[j])
                end = i
                chars.append(' ')
            elif i ==len(s)-1:
                for j in range(i, end, -1):
                    chars.append(s[j])
        return ''.join(chars)


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    print(f"{s }")
    print('----------Answer Below----------')
    print(Solution().reverseWords(s))
