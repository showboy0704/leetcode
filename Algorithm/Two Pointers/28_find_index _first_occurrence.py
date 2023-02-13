class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        left, right = 0, len(needle)
        while right < len(haystack)+1:
            if needle == haystack[left:right]:
                return left
            left += 1
            right += 1
        return -1


if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    print(f"{haystack,needle}")
    print('----------Answer Below----------')
    print(Solution().strStr(haystack, needle))
