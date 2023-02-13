class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        if len(s) == k:
            return k
        char_table = dict(Q=0, A=0, Z=0, W=0, S=0, X=0, E=0, D=0, C=0,
                        R=0, F=0, V=0, T=0, G=0, B=0, Y=0, H=0, N=0,
                        U=0, J=0, M=0, I=0, K=0, O=0, L=0, P=0)
        longest = 1
        left, right = 0, 1
        char_table[s[left]] += 1
        while right < len(s):
            window_length = right-left+1
            char_table[s[right]] += 1
            max_frequecy = max(char_table.values())
            if max_frequecy+k >= window_length:
                longest += 1

            else:
                char_table[s[left]] -= 1
                left += 1
            right += 1
        return longest


if __name__ == '__main__':
    s = "ABAA"
    k = 0
    print(f"{s,k}")
    print(Solution().characterReplacement(s, k))
