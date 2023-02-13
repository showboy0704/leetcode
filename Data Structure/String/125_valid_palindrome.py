class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n-1
        while l <= r:
            if not(s[l].isnumeric() or s[l].isalpha()):
                l += 1
                continue
            if not(s[r].isnumeric() or s[r].isalpha()):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True


if __name__ == '__main__':
    s = s = "A man, a plan, a canal: Panama"
    print(f"{s}")
    print('----------Answer Below----------')
    print(Solution().isPalindrome(s))
