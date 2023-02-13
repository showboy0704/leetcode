class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrypt, i = [], 0
        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                decrypt.append(chr(96+int(s[i:i+2])))
                i += 3
            else:
                decrypt.append(chr(96+int(s[i])))
                i += 1
        return ''.join(decrypt)


if __name__ == '__main__':
    s = "10#11#12"
    print(f"{s}")
    print('----------Answer Below----------')
    print(Solution().freqAlphabets(s))
