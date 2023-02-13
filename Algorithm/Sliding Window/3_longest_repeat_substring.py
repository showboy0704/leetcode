class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_table = dict()
        longest = 0
        for i, char in enumerate(s):
            window_right = i+1
            window_left = i-longest
            char_table[char] = i
            for j in range(window_left, window_right):
                sub_char = s[j]
                add_length = 1
                if not char_table[sub_char] == j:
                    add_length = 0
                    break
            longest += add_length
        return longest


if __name__ == '__main__':
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
    print(f"{s}")
    print(Solution().lengthOfLongestSubstring(s))
