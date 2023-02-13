class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 1:
            if k <= 1:
                return 1
            else:
                return 0
        char_table = dict(q=0, a=0, z=0, w=0, s=0, x=0, e=0, d=0, c=0,
                          r=0, f=0, v=0, t=0, g=0, b=0, y=0, h=0, n=0,
                          u=0, j=0, m=0, i=0, k=0, o=0, l=0, p=0)
        max_unique_char = 0
        for char in s:
            if char_table.get(char) == 0:
                max_unique_char += 1
            char_table[char] += 1

        longest = 0
        for unique_char_num in range(1, max_unique_char+1):
            char_table = dict(q=0, a=0, z=0, w=0, s=0, x=0, e=0, d=0, c=0,
                              r=0, f=0, v=0, t=0, g=0, b=0, y=0, h=0, n=0,
                              u=0, j=0, m=0, i=0, k=0, o=0, l=0, p=0)
            left, right = 0, 1
            current_char_num = 0
            char_table[s[left]] += 1
            current_char_num += 1

            if char_table.get(s[right]) == 0:
                current_char_num += 1
            char_table[s[right]] += 1
            lengths = [v for v in char_table.values() if v > 0]
            if min(lengths) >= k and len(lengths) == unique_char_num:
                length = sum(lengths)
                if length > longest:
                    longest = length
            while right < len(s)-1:

                if current_char_num <= unique_char_num:
                    right += 1
                    if char_table.get(s[right]) == 0:
                        current_char_num += 1
                    char_table[s[right]] += 1
                else:
                    char_table[s[left]] -= 1
                    if char_table.get(s[left]) == 0:
                        current_char_num -= 1
                    left += 1
                print(s[left:right+1])
                lengths = [v for v in char_table.values() if v > 0]
                if min(lengths) >= k and len(lengths) == unique_char_num:
                    length = sum(lengths)
                    if length > longest:
                        longest = length
        return longest


if __name__ == '__main__':
    s = "aabcac"
    k = 2
    print(f"{s}")
    print(Solution().longestSubstring(s, k))
