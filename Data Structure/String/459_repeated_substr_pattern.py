class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)//2+1):
            sub_str = s[:i]
            whole_str = ''
            if len(s) % i == 0:
                for _ in range(len(s)//i):
                    whole_str += sub_str
            if whole_str == s:
                return True

        return False


if __name__ == '__main__':
    s = "abab"
    print(f"{s}")
    print('----------Answer Below----------')
    print(Solution().repeatedSubstringPattern(s))
