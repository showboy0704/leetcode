def is_good(s: str) -> int:
    char_set = set()
    for c in s:
        char_set.add(c)
    return 1 if len(char_set) == 3 else 0


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for l in range(len(s)):
            r = l+3
            count += is_good(s[l:r])
        return count


if __name__ == '__main__':
    s =  "aababcabc"
    print(f"{s}")
    print('----------Answer Below----------')
    print(Solution().countGoodSubstrings(s))
